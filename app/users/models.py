from django.db import models
from django.contrib.postgres.search import SearchVector, SearchVectorField
from django.contrib.postgres.indexes import GinIndex


class User(models.Model):
    last_name = models.CharField("Фамилия", max_length=50)
    first_name = models.CharField("Имя", max_length=50)
    middle_name = models.CharField("Отчество", max_length=50, blank=True, null=True)
    date_of_birth = models.DateField("Дата рождения", blank=True, null=True)
    passport_number = models.CharField("Номер паспорта", max_length=11, unique=True)
    place_of_birth = models.CharField("Место рождения", max_length=255)
    phone_number = models.CharField("Телефон", max_length=12, unique=True)
    email = models.EmailField("Емейл", unique=True)
    registration_address = models.CharField("Адрес регистрации", max_length=255)
    residential_address = models.CharField("Адрес проживания", max_length=255)
    search_vector = SearchVectorField(null=True, editable=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        from django.contrib.postgres.search import SearchVector
        vector = (
            SearchVector('last_name', weight='A', config='russian') +
            SearchVector('first_name', weight='A', config='russian') +
            SearchVector('middle_name', weight='B', config='russian') +
            SearchVector('phone_number', weight='A', config='russian') +
            SearchVector('email', weight='A', config='russian')
        )
        User.objects.filter(pk=self.pk).update(search_vector=vector)

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name or ''}"

    class Meta:
        indexes = [
            GinIndex(fields=['search_vector']),
        ]
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
