# Generated by Django 4.1.3 on 2023-01-19 08:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('atar_goal', models.IntegerField(blank=True, null=True)),
                ('graduation_year', models.IntegerField(blank=True, null=True)),
                ('suburb', models.CharField(blank=True, max_length=100, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, upload_to='profile_image')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('discipline', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.discipline')),
                ('students', models.ManyToManyField(blank=True, to='core.profile')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('suburb', models.CharField(blank=True, max_length=100, null=True)),
                ('students', models.ManyToManyField(blank=True, related_name='students', to='core.profile')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.school'),
        ),
        migrations.AddField(
            model_name='profile',
            name='subjects',
            field=models.ManyToManyField(blank=True, to='core.subject'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]