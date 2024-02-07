from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from web.models import Job, Client, MassageSession, Symptom, MassageType

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
        if Client.objects.get(username=cleaned_data["phone"]):
            self.add_error("phone", "такой номер уже зарегистрирован в системе")
        return cleaned_data

    class Meta:
        model = User
        fields = ("first_name", "last_name", "phone", "age", "password", "confirm_password")


class AuthForm(forms.Form):
    phone = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class SessionForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.client = self.initial["user"]
        return super().save(commit)

    class Meta:
        model = MassageSession
        fields = ("client_symptoms", "massage_type", "session_date", "session_index")


class SymptomForm(forms.ModelForm):
    class Meta:
        model = Symptom
        fields = ("name",)


class MassageTypeForm(forms.ModelForm):
    class Meta:
        model = MassageType
        fields = ("name", "price")


class SessionFilterForm(forms.Form):
    date = forms.DateTimeField(
        label="дата",
        widget=forms.DateTimeInput(
            attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M"
        ),
        required=False,
    )
    index = forms.IntegerField(
        label="Номер сеанса",
        required=False
    )
    type = forms.ModelChoiceField(
        label="Тип массажа",
        queryset=MassageType.objects.all(),
        required=False
    )
