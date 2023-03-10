# Generated by Django 4.1.3 on 2023-01-30 03:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correct', models.IntegerField()),
                ('total_questions', models.IntegerField()),
                ('study_session', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('self_marked', models.BooleanField(default=False)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject', to='core.subject')),
                ('taker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taker', to='core.profile')),
            ],
        ),
    ]
