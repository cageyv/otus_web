# Generated by Django 3.0.2 on 2020-01-29 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ('-graduated', 'last_name')},
        ),
        migrations.RemoveField(
            model_name='student',
            name='year_in_school',
        ),
    ]