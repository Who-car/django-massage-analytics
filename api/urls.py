from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import SimpleRouter

from api.views import main_view, SessionModelViewSet, SymptomsViewSet

router = SimpleRouter()
router.register("sessions", SessionModelViewSet, basename="sessions")
router.register("symptoms", SymptomsViewSet, basename="symptoms")

urlpatterns = [path("", main_view), path("token/", obtain_auth_token), *router.urls]
