from django.db import models
from django.contrib.auth.models import User
from django_unixdatetimefield import UnixDateTimeField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    school = models.ForeignKey('School', on_delete=models.CASCADE, blank=True, null=True)
    atar_goal = models.IntegerField(blank=True, null=True)
    graduation_year = models.IntegerField(blank=True, null=True)
    subjects = models.ManyToManyField('Subject', blank=True)
    suburb = models.CharField(max_length=100, blank=True, null=True) # city, suburb, town etc
    zip_code = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return self.user.username

class Subject(models.Model):
    name = models.CharField(max_length=100)
    discipline = models.ForeignKey('Discipline', on_delete=models.CASCADE, blank=True, null=True)
    students = models.ManyToManyField('Profile', blank=True)
    def __str__(self):
        return self.name

class Discipline(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class School(models.Model):
    name = models.CharField(max_length=100)
    suburb = models.CharField(max_length=100, blank=True, null=True) # city, suburb, town etc
    students = models.ManyToManyField(Profile, blank=True, related_name='students')
    def __str__(self):
        return self.name

import datetime

class Assessment(models.Model):
    taker = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='taker')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subject')
    correct = models.IntegerField()
    total_questions = models.IntegerField()
    study_session = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    start_time = models.CharField(max_length=256)
    end_time = models.CharField(max_length=256)
    self_marked = models.BooleanField(default=False)

    @property
    def time_taken(self):
        converted_ed = datetime.datetime.fromtimestamp(float(self.end_time))
        converted_sd = datetime.datetime.fromtimestamp(float(self.start_time))
        return (converted_ed - converted_sd).total_seconds()
    def __str__(self):
        return self.taker.name + ' ' + self.subject.name