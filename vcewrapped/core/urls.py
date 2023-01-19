from django.contrib import admin
from django.urls import path, include
from core.views import index
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]