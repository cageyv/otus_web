# Generated by Django 2.2.9 on 2020-02-29 15:36

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20200217_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='started',
            field=models.DateTimeField(default=django.utils.timezone.now, validators=[django.core.validators.MinValueValidator(datetime.datetime(1969, 12, 31, 21, 0, tzinfo=utc)), django.core.validators.MaxValueValidator(django.utils.timezone.now)], verbose_name='Дата начала'),
        ),
    ]
