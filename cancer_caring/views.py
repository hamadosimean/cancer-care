from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
import bleach
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    """Render the index page."""

    context = {
        "infos": [
            {
                "title": "Qu’est-ce que le cancer du sein ?",
                "content": "Le cancer du sein est une maladie où des cellules anormales se développent dans les tissus mammaires. C’est le cancer le plus fréquent chez les femmes, mais il peut aussi toucher les hommes.",
                "image": "https://via.placeholder.com/400x250?text=Cancer+du+sein",
            },
            {
                "title": "Facteurs de risque",
                "content": "Parmi les principaux facteurs de risque figurent l’âge, les antécédents familiaux, les mutations génétiques (BRCA1/BRCA2), une alimentation déséquilibrée, l’obésité, le tabac et l’alcool.",
                "image": "https://via.placeholder.com/400x250?text=Facteurs+de+risque",
            },
            {
                "title": "Prévention",
                "content": "Un mode de vie sain réduit les risques : alimentation équilibrée, activité physique régulière, limitation du tabac et de l’alcool, allaitement et suivi médical régulier.",
                "image": "https://via.placeholder.com/400x250?text=Prévention",
            },
            {
                "title": "Dépistage",
                "content": "Le dépistage précoce augmente considérablement les chances de guérison. Les mammographies et l’auto-examen des seins sont fortement recommandés à partir d’un certain âge.",
                "image": "https://via.placeholder.com/400x250?text=Dépistage",
            },
        ]
    }

    return render(request, "index.html", context)


def register_view(request):
    """Render the registration page."""
    if request.method == "POST":
        username = bleach.clean(request.POST.get("username"))
        email = bleach.clean(request.POST.get("email"))
        password = bleach.clean(request.POST.get("password"))
        first_name = bleach.clean(request.POST.get("first_name"))
        last_name = bleach.clean(request.POST.get("last_name"))

        if not username or not email or not password:
            messages.error(request, "Veuillez saisir tous les informations")
        else:
            User.objects.create_user(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=password,
            )
            messages.success(request, "Votre compte a été créé avec succès")
            return redirect("login")

    return render(request, "cancer_caring/pages/register.html")


def login_view(request):
    """Render the login page."""
    if request.method == "POST":
        username = bleach.clean(request.POST.get("username"))
        password = bleach.clean(request.POST.get("password"))
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("index")
            messages.error(request, "Votre compte est inactif.")
            return redirect("index")
        messages.error(request, "Identifiants invalides.")
    return render(request, "cancer_caring/pages/login.html")


def logout_view(request):
    """Render the logout page."""
    logout(request)
    messages.success(request, "Vous avez été déconnecté avec succès.")
    return render(request, "cancer_caring/pages/logout.html")


@login_required(login_url="/login/")
def profile_view(request):
    """Render the user profile page."""
    return render(request, "cancer_caring/pages/profile.html")


def about_view(request):
    """Render the about page."""
    return render(request, "cancer_caring/pages/about.html")


def advice_view(request):
    """Render the advice page."""
    return render(request, "cancer_caring/pages/advice.html")


@login_required(login_url="/login/")
def consultation_view(request):
    """Render the consultation page."""
    return render(request, "cancer_caring/pages/consultation.html")
