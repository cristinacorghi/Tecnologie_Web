from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
from django.urls import reverse_lazy
from django.views.generic import CreateView
from forms.loginForm import UserLoginForm


def Base(request):
    return render(request, 'homepage.html')


def login_view(request):
    next = request.GET.get('next')
    title = 'Login'
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')
    return render(request, 'login.html', {'form': form, 'title': title})


class UserCreationView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('/')


def logout_view(request):
    logout(request)
    return redirect('/')
