# Generated by Django 5.1.3 on 2024-11-14 16:58

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=75)),
                ('message', models.TextField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=75)),
                ('gradeSection', models.CharField(max_length=40)),
                ('completed', models.BooleanField(default=False)),
                ('dateSubmitted', models.DateTimeField(default=django.utils.timezone.now)),
                ('damagedProperty', models.CharField(choices=[('chair', 'Chair'), ('table', 'Table'), ('electricfan', 'Electric Fan'), ('outlet', 'Outlet'), ('television', 'Television'), ('whiteboard', 'Whiteboard'), ('tiles', 'Tiles'), ('window', 'Window')], default='chair', max_length=50)),
                ('comment', models.SlugField(blank=True, null=True)),
            ],
        ),
    ]
