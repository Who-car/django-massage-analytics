from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend

User = get_user_model()


class PhoneAuthBackend(BaseBackend):
    def authenticate(self, request, phone=None, password=None):
        try:
            user = User.objects.get(phone=phone)
        except User.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
