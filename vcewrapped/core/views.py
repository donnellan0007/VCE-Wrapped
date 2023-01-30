from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from core.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, AssessmentForm
from core.models import Profile, Assessment, Subject
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return render(request, 'core/index.html')
    else:
        return redirect('core:register')

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
                return redirect('core:update-profile')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'core/register.html', {'form': form})

def update_profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            form.save()
            return redirect('core:index')
    else:
        form = ProfileUpdateForm(instance=profile)
    return render(request, 'core/profile-update.html', {'form': form})

def new_assessment(request):
    print(request.user.profile)
    classes = Subject.objects.filter(profile=request.user.profile)
    if request.method == 'POST':
        form = AssessmentForm(request.POST, profile=request.user.profile)
        if form.is_valid():
            form.taker = request.user.profile
            form.save()
            return redirect('core:index')
    else:
        form = AssessmentForm(profile=request.user.profile)
    return render(request, 'core/new-assessment.html', {'form': form, 'classes': classes,})