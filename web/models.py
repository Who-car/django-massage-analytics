from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class Jobs(models.Model):
    job_name = models.CharField(max_length=64)


class JobActivity(models.Model):
    job_activity_name = models.CharField(max_length=64)


class Client(AbstractUser):
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    job_activity = models.ForeignKey(JobActivity, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=128)
    client_phone = models.CharField(max_length=11)
    client_age = models.IntegerField()


User = get_user_model()


class MassageTypes(models.Model):
    massage_type_name = models.CharField(max_length=64)


class Symptoms(models.Model):
    symptom_name = models.CharField(max_length=256)


class MassageSessions(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    client_symptoms = models.ManyToManyField(Symptoms)
    massage_type = models.ForeignKey(MassageTypes, on_delete=models.CASCADE)
    session_date = models.DateField()
    session_index = models.IntegerField()
