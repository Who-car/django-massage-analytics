from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from web.forms import RegistrationForm, AuthForm
from web.models import Client, Job


def main_view(request):
    return render(request, 'web/main.html', {
        "year": datetime.now().year
    })


def registration_view(request):
    form = RegistrationForm()
    is_success = False
    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            job_obj = Job.objects.get(job_name=form.cleaned_data["job"])
            print(f'job_obj is {job_obj}')
            user = Client(
                username=form.cleaned_data["phone"],
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                phone=form.cleaned_data["phone"],
                age=form.cleaned_data["age"],
                job=job_obj,
                job_activity=form.cleaned_data["job_activity"],
            )
            user.set_password(form.cleaned_data["password"])
            user.save()
            is_success = True
    return render(
        request, "web/registration.html", {"form": form, "is_success": is_success}
    )


def auth_view(request):
    form = AuthForm()
    if request.method == "POST":
        form = AuthForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data["phone"], password=form.cleaned_data["password"])
            print(form.cleaned_data)
            if user is None:
                form.add_error(None, "Введены неверные данные")
            else:
                login(request, user)
                return redirect("main")
    return render(request, "web/auth.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect('main')
