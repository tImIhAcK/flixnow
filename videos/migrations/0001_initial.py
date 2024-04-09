# Generated by Django 5.0.2 on 2024-04-09 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Video",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                (
                    "description",
                    models.TextField(blank=True, max_length=2500, null=True),
                ),
                ("video_id", models.CharField(max_length=60, unique=True)),
                ("slug", models.SlugField(blank=True, null=True)),
                ("active", models.BooleanField(default=True)),
                (
                    "state",
                    models.CharField(
                        choices=[("PU", "Publish"), ("DR", "Draft")],
                        default="DR",
                        max_length=2,
                    ),
                ),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("publish_timestamp", models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="VideoProxy",
            fields=[],
            options={
                "verbose_name": "published video",
                "verbose_name_plural": "published videos",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("videos.video",),
        ),
    ]
