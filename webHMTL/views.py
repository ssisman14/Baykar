from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, LoginForm
from api.models import User
from django.shortcuts import render, get_object_or_404
import random
from django.core.mail import EmailMessage


# Create your views here.
def app(request):
    return render(request, 'main.html')


def ilanlarim(request):
    return render(request, 'ilan.html')


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


def login_isveren(request):

    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():

        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        user_info = User.objects.get(username=username)

        if user is None:
            messages.info(request, 'kullanıcı adı veya şifre hatalı')
            return render(request, 'login_user.html', context)

        messages.success(request, 'Giriş Yapıldı')

        if user_info.durum == 'isveren':
            login(request, user)
            return redirect('app')

    return render(request, 'login_isveren.html', context)


def logout_user(request):
    logout(request)
    return redirect('app')


def forgot_password(request):
    context = {}
    if request.method == "POST":
        un = request.POST["username"]
        pwd = request.POST["npassword"]
        print(un, pwd)
        user = get_object_or_404(User, username=un)
        user.set_password(pwd)
        user.save()
        context["status"] = "şifre başarıyla değiştirildi.."
    return render(request, "forgot_pass.html", context)


def reset_password(request):
    un = request.GET['username']
    try:
        user = get_object_or_404(User, username=un)
        otp = random.randint(1000, 9999)
        msz = "Değerli Kullanıcımız {} \n{} tek seferlik şifreniz \nBaşkalarıyla paylaşmayınız \n Saygılarımızla ".format(
            user.username, otp)
        try:
            email = EmailMessage("Account Verification", msz, to=[user.email])
            email.send()
            return JsonResponse({"status": "sent", "email": user.email, "rotp": otp})
        except:
            return JsonResponse({"status": "error", "email": user.email})

        # return HttpResponse(user.email)
    except:
        return JsonResponse({"status": 'failed'})