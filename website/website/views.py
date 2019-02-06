from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
import views
from django.http import HttpResponseRedirect

def gotobooks(request):
    return HttpResponseRedirect('/books/')

def home_page(request):
    return render(request,'home_page.html')

def login_page(request):
    login_form = LoginForm(request.POST or None)
    context = {'form' : login_form}
    if login_form.is_valid():
        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            context['error'] = "Incorrect Password"
    return render(request, 'login.html', context)

User = get_user_model()

def register_page(request):
    register_form = RegisterForm(request.POST or None)
    context = {'form' : register_form}
    if register_form.is_valid():
        username = register_form.cleaned_data.get('username')
        email    = register_form.cleaned_data.get('email')
        password = register_form.cleaned_data.get('password')
        user = User.objects.create_user(username, email, password)
        return redirect('home')
    return render(request, 'register.html', context)