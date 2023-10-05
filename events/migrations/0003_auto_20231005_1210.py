# Generated by Django 3.2.21 on 2023-10-05 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20231005_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(choices=[('Conference', 'Conference'), ('Networking', 'Networking'), ('Panel', 'Panel'), ('Product launch', 'Product launch'), ('Talk', 'Talk'), ('Workshop', 'Workshop'), ('Other', 'Other')], default='n/a', max_length=50),
        ),
        migrations.AlterField(
            model_name='event',
            name='format',
            field=models.CharField(choices=[('In person', 'In person'), ('Hybrid', 'Hybrid'), ('Online', 'Online')], default='n/a', max_length=50),
        ),
    ]
