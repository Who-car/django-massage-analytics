import random
from datetime import timedelta
from random import randint

from django.core.management.base import BaseCommand
from django.utils.timezone import now

from web.models import MassageSession, Client, Symptom, MassageType


class Command(BaseCommand):
    def handle(self, *args, **options):
        current_date = now()
        user = Client.objects.filter(username="0").first()
        symptoms = Symptom.objects.all()
        massage_types = MassageType.objects.all()

        sessions = []

        for day_index in range(30):
            current_date -= timedelta(days=1)

            for session_index in range(randint(5, 10)):
                sessions.append(
                    MassageSession(
                        session_date=current_date,
                        session_index=session_index,
                        massage_type=massage_types[randint(0, 3)],
                        client=user,
                    )
                )

        saved_time_sessions = MassageSession.objects.bulk_create(sessions)
        client_symptoms = []
        for session in saved_time_sessions:
            count_of_symptoms = randint(0, len(symptoms))
            for symptom_index in range(count_of_symptoms):
                client_symptoms.append(
                    MassageSession.client_symptoms.through(
                        massagesession_id=session.id, symptom_id=symptoms[symptom_index].id
                    )
                )
        MassageSession.client_symptoms.through.objects.bulk_create(client_symptoms)