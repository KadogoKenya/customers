# Generated by Django 4.2.7 on 2023-11-08 17:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customerDetails", "0002_alter_business_phone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="business",
            name="businessAge",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(120),
                ]
            ),
        ),
        migrations.AlterField(
            model_name="business",
            name="date_of_birth",
            field=models.DateField(max_length=30),
        ),
    ]
