from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, PasswordInput
from django_select2 import forms as s2forms

from .models import Profile, Subject, Discipline, School, Assessment
from django.core.mail import send_mail
from django.conf import settings

class SchoolWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "name__icontains",
    ]

class SubjectWidget(s2forms.ModelSelect2MultipleWidget):
    search_fields = [
        "name__icontains",
    ]

from django.db.models import Q

class AssessmentWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "taker.subject.name__icontains",
    ]

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    # placeholders

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': TextInput(attrs={'placeholder': 'Last Name'}),
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
        fields = ['phone', 'address', 'school', 'subjects', 'atar_goal', 'graduation_year']
        widgets = {
            "school": SchoolWidget,
            "subjects": SubjectWidget,
        }

class AssessmentForm(forms.ModelForm):

    class Meta:
        model = Assessment
        fields = ['subject', 'correct', 'total_questions', 'study_session', 'start_time', 'end_time', 'self_marked']
        widgets = {
            # "subject": AssessmentWidget,
        }
    def __init__(self, taker, *args, **kwargs):
        super(AssessmentForm, self).__init__(*args, **kwargs)
        self.fields['subject'].queryset = Assessment.objects.filter(taker=taker)