# Generated by Django 2.2.9 on 2020-03-01 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessongrade',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Student'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='courses.Course'),
        ),
        migrations.AddField(
            model_name='coursegrade',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course'),
        ),
        migrations.AddField(
            model_name='coursegrade',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Student'),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='profiles.Teacher', verbose_name='Преподаватель'),
        ),
    ]
