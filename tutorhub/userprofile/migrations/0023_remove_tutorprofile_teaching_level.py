# Generated by Django 4.2.3 on 2023-08-24 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("userprofile", "0022_alter_teachinglevel_teaching_level"),
    ]

    operations = [
        migrations.RemoveField(model_name="tutorprofile", name="teaching_level",),
    ]
