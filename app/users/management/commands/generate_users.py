from django.contrib.postgres.search import SearchVector
from django.core.management.base import BaseCommand
from faker import Faker
from users.models import User


class Command(BaseCommand):
    help = 'Генерирует случайных пользователей и добавляет их в базу данных'

    def handle(self, *args, **kwargs):
        if User.objects.exists():
            self.stdout.write(self.style.SUCCESS("Пользователи уже существуют. Пропуск генерации."))
            return

        fake = Faker('ru_RU')
        num_users = 100000  # Количество пользователей для генерации

        # Множества для проверки уникальности
        emails = set()
        phone_numbers = set()
        passport_numbers = set()
        len_users = 0

        users = []
        while len_users < num_users:
            email = fake.email()
            phone_number = f"7{fake.random_number(digits=10, fix_len=True)}"
            passport_number = f"{fake.random_number(digits=4, fix_len=True)} {fake.random_number(digits=6, fix_len=True)}"

            # Проверка уникальности email, phone_number и passport_number
            if email in emails or User.objects.filter(email=email).exists():
                email = None
            if phone_number in phone_numbers or User.objects.filter(phone_number=phone_number).exists():
                phone_number = None
            if passport_number in passport_numbers or User.objects.filter(passport_number=passport_number).exists():
                passport_number = None

            if email and phone_number and passport_number:
                emails.add(email)
                phone_numbers.add(phone_number)
                passport_numbers.add(passport_number)

                user = User(
                    last_name=fake.last_name(),
                    first_name=fake.first_name(),
                    middle_name=fake.middle_name(),
                    date_of_birth=fake.date_of_birth(minimum_age=18, maximum_age=90),
                    passport_number=passport_number,
                    place_of_birth=fake.city(),
                    phone_number=phone_number,
                    email=email,
                    registration_address=fake.address(),
                    residential_address=fake.address()
                )
                users.append(user)
                len_users += 1

            # Используем bulk_create для массового создания объектов
            if len(users) >= 10000:  # Периодическая загрузка в базу
                User.objects.bulk_create(users)
                self.stdout.write(self.style.SUCCESS(f"Добавлено {len(users)} пользователей в базу данных"))
                users = []

        # Последняя загрузка в базу данных, если остались незаписанные пользователи
        if users:
            User.objects.bulk_create(users)
            self.stdout.write(self.style.SUCCESS(f"Добавлено {len(users)} пользователей в базу данных"))

        # Обновляем search_vector после массового создания
        self._update_search_vector()

        self.stdout.write(self.style.SUCCESS(f"Успешно добавлено {num_users} пользователей в базу данных"))

    @staticmethod
    def _update_search_vector():
        # Обновляем search_vector для всех пользователей
        vector = (
                SearchVector('last_name', weight='A', config='russian') +
                SearchVector('first_name', weight='A', config='russian') +
                SearchVector('middle_name', weight='B', config='russian') +
                SearchVector('phone_number', weight='A', config='russian') +
                SearchVector('email', weight='A', config='russian')
        )
        User.objects.update(search_vector=vector)
