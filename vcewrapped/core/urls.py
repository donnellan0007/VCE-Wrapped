from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core.views import index, register, update_profile, new_assessment
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('register/your-vce', views.update_profile, name='update-profile'),
    path('assessment/new', views.new_assessment, name='new-assessment'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)