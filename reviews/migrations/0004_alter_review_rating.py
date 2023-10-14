# Generated by Django 3.2.21 on 2023-10-14 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_alter_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.CharField(choices=[('5 stars', '5 stars'), ('4 stars', '4 stars'), ('3 stars', '3 stars'), ('2 stars', '2 stars'), ('1 star', '1 star'), ('0 stars', '0 stars')], default='5 stars', max_length=50),
        ),
    ]
