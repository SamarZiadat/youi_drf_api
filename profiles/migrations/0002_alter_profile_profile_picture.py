# Generated by Django 3.2.21 on 2023-10-04 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='../user_q6u7m3', upload_to='images/'),
        ),
    ]
