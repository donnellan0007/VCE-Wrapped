from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
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

class Assessment(models.Model):
    taker = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='taker')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subject')
    correct = models.IntegerField()
    total_questions = models.IntegerField()
    study_session = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    self_marked = models.BooleanField(default=False)
    def __str__(self):
        return self.taker.name + ' ' + self.subject.name