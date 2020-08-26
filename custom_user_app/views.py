from django.shortcuts import render, HttpResponseRedirect, reverse
from custom_user_app.models import CustomUser
from custom_user_app.forms import LoginForm, SignupForm
from django.contrib.auth import authenticate, login, logout
from custom_user.settings import AUTH_USER_MODEL


def index(request):
    return render(request, "index.html", {"result": AUTH_USER_MODEL})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get("username"), password=data.get("password"))
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("homepage"))

    form = LoginForm()
    return render(request, "login.html", {"form": form})


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = CustomUser.objects.create_user(
                username=data.get("username"),
                password=data.get("password"),
                displayname=data.get("displayname"),
            )
            login(request, user)
            return HttpResponseRedirect(reverse("homepage"))

    form = SignupForm()
    return render(request, "signup.html", {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))




