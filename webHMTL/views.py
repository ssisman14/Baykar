from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth import login
from .forms import RegisterForm
from api.models import User


# Create your views here.
def app(request):
    return render(request, 'main.html')

def user_login(request):
    return render(request, 'login_user.html')

def user_sing_in(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('username')
            durum = form.cleaned_data.get('durum')
            print(durum)

            newUser = User(username=username, durum=durum)

            newUser.set_password(password)
            newUser.save()
            login(request, newUser)
            return redirect("app")
        context = {
            "form": form
        }
        return render(request, 'sing_in_user.html', context)
    else:
        form = RegisterForm()
        context = {
            "form": form
        }
        return render(request, 'sing_in_user.html', context)




