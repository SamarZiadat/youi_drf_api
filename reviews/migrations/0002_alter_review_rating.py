# Generated by Django 3.2.21 on 2023-10-14 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.CharField(choices=[('5 stars', '5 stars'), ('4 stars', '4 stars'), ('3 stars', '3 stars'), ('2 stars', '2 stars'), ('1 stars', '1 stars'), ('0 stars', '0 stars')], default='5/5', max_length=50),
        ),
    ]
