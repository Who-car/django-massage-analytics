from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class Job(models.Model):
    name = models.CharField(max_length=64, verbose_name="Профессия", default='безработный')

    def __str__(self):
        return self.name


class Client(AbstractUser):
    ACTIVE = 'Active'
    PASSIVE = 'Passive'
    HYBRID = 'Hybrid'
    JOB_ACTIVITIES = (
        (ACTIVE, 'Подвижная работа'),
        (PASSIVE, 'Сидячая работа'),
        (HYBRID, 'Смешанная работа'),
    )

    first_name = models.CharField(verbose_name="Имя", default="first_name")
    last_name = models.CharField(verbose_name="Фамилия", default="last_name")
    phone = models.CharField(
        verbose_name="Номер телефона",
        default="00000000000",
        validators=[
            RegexValidator(r'^\d{11}$', message='Номер телефона должен содержать 11 цифр')
        ])
    age = models.IntegerField(verbose_name="Возраст", default=0)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, verbose_name="Профессия", default=0)
    job_activity = models.CharField(verbose_name="Характер работы", default=PASSIVE, choices=JOB_ACTIVITIES)


User = get_user_model()


class MassageType(models.Model):
    name = models.CharField(max_length=64, verbose_name="Тип массажа")
    price = models.IntegerField(verbose_name="Цена", default=0)

    def __str__(self):
        return f'{self.name} - {self.price}р.'


class Symptom(models.Model):
    name = models.CharField(max_length=256, verbose_name="Симптом")

    def __str__(self):
        return self.name


class MassageSession(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Клиент")
    client_symptoms = models.ManyToManyField(Symptom, verbose_name="Симптомы")
    massage_type = models.ForeignKey(MassageType, on_delete=models.CASCADE, verbose_name="Тип массажа")
    session_date = models.DateField(verbose_name="Дата сеанса")
    session_index = models.IntegerField(verbose_name="Номер сеанса")
