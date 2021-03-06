# Generated by Django 3.1.3 on 2020-12-15 18:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carpark', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slotsall',
            name='slotno',
            field=models.IntegerField(unique=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)]),
        ),
        migrations.AlterField(
            model_name='slotsall',
            name='totalslots',
            field=models.PositiveIntegerField(default=20, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)]),
        ),
    ]
