# Generated by Django 4.2.3 on 2023-08-24 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userprofile", "0020_alter_tutorprofile_bio"),
    ]

    operations = [
        migrations.AlterField(
            model_name="teachinglevel",
            name="teaching_level",
            field=models.CharField(max_length=60),
        ),
    ]
