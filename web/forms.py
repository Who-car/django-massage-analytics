from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from web.models import Job, Client

User = get_user_model()


class RegistrationForm(forms.ModelForm):
    job = forms.ModelChoiceField(queryset=Job.objects.all())
    job_activity = forms.ChoiceField(choices=Client.JOB_ACTIVITIES)
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data["password"] != cleaned_data["confirm_password"]:
            self.add_error("password", "Пароли не совпадают")
        return cleaned_data

    class Meta:
        model = User
        fields = ("first_name", "last_name", "phone", "age", "password", "confirm_password")


class AuthForm(forms.Form):
    phone = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
