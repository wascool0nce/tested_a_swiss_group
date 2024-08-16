from django.db import models


# Create your models here.
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

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name or ''}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"