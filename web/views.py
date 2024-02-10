from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import user_passes_test
from web.forms import RegistrationForm, AuthForm, SessionForm, SymptomForm, MassageTypeForm, SessionFilterForm
from web.models import Client, Job, MassageSession, Symptom, MassageType
from web.services import filter_sessions, get_stat


def main_view(request):
    massage_types = MassageType.objects.all().order_by("price")

    return render(
        request,
        "web/main.html",
        {
            "massage_types": massage_types
        },
    )


def sessions_view(request):
    sessions = MassageSession.objects.filter(client=request.user).order_by("-session_date")

    filter_form = SessionFilterForm(request.GET)
    filter_form.is_valid()
    sessions = filter_sessions(sessions, filter_form.cleaned_data)

    total_count = sessions.count()
    sessions = (
        sessions.prefetch_related("client_symptoms")
        .select_related("client")
        .annotate(symptoms_count=Count("client_symptoms"))
    )
    page_number = request.GET.get("page", 1)

    paginator = Paginator(sessions, per_page=100)

    return render(
        request,
        "web/sessions.html",
        {
            "sessions": paginator.get_page(page_number),
            "form": SessionForm(),
            "filter_form": filter_form,
            "total_count": total_count
        },
    )


def registration_view(request):
    form = RegistrationForm()
    is_success = False
    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = Client(
                username=form.cleaned_data["phone"],
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                phone=form.cleaned_data["phone"],
                age=form.cleaned_data["age"],
                job=Job.objects.get(name=form.cleaned_data["job"]),
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
            user = authenticate(**form.cleaned_data)
            if user is None:
                form.add_error(None, "Введены неверные данные")
            else:
                login(request, user)
                # if user.is_superuser:
                #     return redirect("admin")
                return redirect("main")
    return render(request, "web/auth.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect('main')


@login_required(login_url='auth')
def session_edit_view(request, id=None):
    session = (
        get_object_or_404(MassageSession, client=request.user, id=id)
        if id is not None
        else None
    )
    form = SessionForm(instance=session)
    if request.method == "POST":
        form = SessionForm(
            data=request.POST,
            files=request.FILES,
            instance=session,
            initial={"user": request.user},
        )
        if form.is_valid():
            form.save()
            return redirect("main")
    return render(request, "web/session_form.html", {"form": form})


@login_required
def session_delete_view(request, id):
    tag = get_object_or_404(MassageSession, user=request.user, id=id)
    tag.delete()
    return redirect("main")


@login_required
def symptoms_view(request):
    symptoms = Symptom.objects.all()
    form = SymptomForm()
    if request.method == "POST":
        form = SymptomForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("symptoms")
    return render(request, f"web/symptoms.html", {"symptoms": symptoms, "form": form})


@login_required
def symptoms_delete_view(request, id):
    symptom = get_object_or_404(Symptom, id=id)
    symptom.delete()
    return redirect("symptoms")


@user_passes_test(lambda u: u.is_superuser, login_url='/auth/')
def massage_types_view(request):
    massage_types = MassageType.objects.all()
    form = MassageTypeForm()
    if request.method == "POST":
        form = MassageTypeForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("massages")
    return render(request, f"web/massage_types.html", {"massage_types": massage_types, "form": form})


@user_passes_test(lambda u: u.is_superuser, login_url='/auth/')
def massage_types_delete_view(request, id):
    massage_type = get_object_or_404(MassageType, id=id)
    massage_type.delete()
    return redirect("massages")
