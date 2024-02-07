from rest_framework import serializers

from web.models import Client, MassageSession, Symptom


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ("id", "first_name", "last_name", "phone")


class SymptomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Symptom
        fields = ("id", "name")


class SessionSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)
    symptoms = SymptomSerializer(many=True, read_only=True)
    symptom_ids = serializers.PrimaryKeyRelatedField(
        queryset=Symptom.objects.all(), many=True, write_only=True
    )

    def save(self, **kwargs):
        symptoms = self.validated_data.pop("symptom_ids")
        self.validated_data["client_id"] = self.context["request"].user.id
        instance = super().save(**kwargs)
        instance.symptoms.set(symptoms)
        return instance

    class Meta:
        model = MassageSession
        fields = ("id", "session_date", "session_index", "massage_type", "symptoms", "client", "symptom_ids")
