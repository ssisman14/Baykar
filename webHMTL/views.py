from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, LoginForm
from api.models import User


# Create your views here.
def app(request):
    return render(request, 'main.html')


def user_login(request):
    form = LoginForm(request.POST or None)

    context = {
        "form": form
    }
    if form.is_valid():

        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)

        if user is None:
            messages.info(request, 'kullanıcı adı veya şifre hatalı')
            return render(request, 'login_user.html', context)

        messages.success(request, 'Giriş Yapıldı')
        login(request, user)
        return redirect('app')

    return render(request, 'login_user.html', context)


def user_sing_in(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        durum = form.cleaned_data.get('durum')

        newUser = User(username=username, durum=durum)
        newUser.set_password(password)
        newUser.save()
        login(request, newUser)
        return redirect("app")
    context = {
        "form": form
    }
    return render(request, 'sing_in_user.html', context)


def logout_user(request):
    logout(request)
    return redirect('app')