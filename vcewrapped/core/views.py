from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from core.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('core:index')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'core/register.html', {'form': form})