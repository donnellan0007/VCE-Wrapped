from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, PasswordInput

from .models import Profile, Subject, Discipline, School
from django.core.mail import send_mail
from django.conf import settings

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    # placeholders

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': TextInput(attrs={'placeholder': 'Username'}),
            'email': EmailInput(attrs={'placeholder': 'Email'}),
            'password1': PasswordInput(attrs={'placeholder': 'Password'}),
            'password2': TextInput(attrs={'placeholder': 'Confirm Password'}),
        }

    def clean(self):
        cleaned_data = super(UserRegisterForm, self).clean()
        email = cleaned_data.get('email')
        username = cleaned_data.get('username')
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'phone', 'address', 'school', 'subjects', 'suburb', 'zip_code', 'image']

