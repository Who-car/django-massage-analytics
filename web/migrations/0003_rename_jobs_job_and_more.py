# Generated by Django 5.0.1 on 2024-02-01 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_remove_client_client_age_remove_client_client_name_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Jobs',
            new_name='Job',
        ),
        migrations.RenameModel(
            old_name='MassageSessions',
            new_name='MassageSession',
        ),
        migrations.RenameModel(
            old_name='MassageTypes',
            new_name='MassageType',
        ),
        migrations.RenameModel(
            old_name='Symptoms',
            new_name='Symptom',
        ),
    ]