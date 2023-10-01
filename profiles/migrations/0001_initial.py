# Generated by Django 3.2.21 on 2023-10-01 11:21

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
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('location', models.CharField(blank=True, max_length=255)),
                ('portfolio_url', models.URLField(blank=True, max_length=255)),
                ('job_title', models.CharField(blank=True, max_length=255)),
                ('current_employer', models.CharField(blank=True, max_length=255)),
                ('about', models.TextField(blank=True)),
                ('work_experience', models.TextField(blank=True)),
                ('education', models.TextField(blank=True)),
                ('certifications', models.TextField(blank=True)),
                ('profile_picture', models.ImageField(default='../default_profile_xbjblo', upload_to='images/')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
