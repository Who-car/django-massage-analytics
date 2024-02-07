from rest_framework.decorators import api_view, permission_classes
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from api.serializers import SessionSerializer, SymptomSerializer
from web.models import MassageSession, Symptom


@api_view(["GET"])
@permission_classes([])
def main_view(request):
    return Response({"status": "ok"})


class SessionModelViewSet(ModelViewSet):
    serializer_class = SessionSerializer

    def get_queryset(self):
        return (
            MassageSession.objects.all()
            .select_related("client")
            .prefetch_related("client_symptoms")
            .filter(client=self.request.user)
        )


class SymptomsViewSet(ListModelMixin, CreateModelMixin, GenericViewSet):
    serializer_class = SymptomSerializer

    def get_queryset(self):
        return Symptom.objects.all()
