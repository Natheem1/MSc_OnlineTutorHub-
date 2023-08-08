# Generated by Django 4.2.3 on 2023-08-08 20:53

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                ("name", models.CharField(max_length=200)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Subject",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField(blank=True, null=True)),
                ("vote_total", models.IntegerField(blank=True, default=0, null=True)),
                ("vote_ratio", models.IntegerField(blank=True, default=0, null=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("tags", models.ManyToManyField(blank=True, to="subjects.tag")),
            ],
            options={"ordering": ["created"],},
        ),
        migrations.CreateModel(
            name="Review",
            fields=[
                ("body", models.TextField(blank=True, null=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "value",
                    models.CharField(
                        choices=[("up", "Positive Vote"), ("down", "Negative Vote")],
                        max_length=20,
                    ),
                ),
                (
                    "subject",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="subjects.subject",
                    ),
                ),
            ],
        ),
    ]
