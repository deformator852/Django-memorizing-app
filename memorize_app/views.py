from django.shortcuts import redirect, render
from .forms import UserRegistrationForm


def index(request):
    return render(request, "memorize_app/index.html")


def login(request):
    return render(request, "memorize_app/login.html")


def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            return render(request, "memorize_app/success_registration.html")
    else:
        form = UserRegistrationForm()
    return render(request, "memorize_app/registration.html", {"form": form})
