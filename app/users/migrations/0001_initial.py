# Generated by Django 3.2.7 on 2024-08-15 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('middle_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Отчество')),
                ('date_of_birth', models.DateField(verbose_name='Дата рождения')),
                ('passport_number', models.CharField(max_length=11, unique=True, verbose_name='Номер паспорта')),
                ('place_of_birth', models.CharField(max_length=255, verbose_name='Место рождения')),
                ('phone_number', models.CharField(max_length=12, unique=True, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Емейл')),
                ('registration_address', models.CharField(max_length=255, verbose_name='Адрес регистрации')),
                ('residential_address', models.CharField(max_length=255, verbose_name='Адрес проживания')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
