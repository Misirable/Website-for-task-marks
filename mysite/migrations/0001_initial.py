# Generated by Django 4.1.3 on 2022-11-08 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
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
                ("Name", models.CharField(max_length=200)),
                ("Age", models.IntegerField()),
                (
                    "Sex",
                    models.CharField(
                        choices=[("NONE", "none"), ("M", "men"), ("W", "women")],
                        default="NONE",
                        max_length=4,
                    ),
                ),
                (
                    "Group",
                    models.CharField(
                        choices=[
                            ("NONE", "none"),
                            ("KI19-11B", "ki19-11b"),
                            ("KI19-12B", "ki19-12b"),
                            ("KI19-13B", "ki19-13b"),
                            ("KI19-14B", "ki19-14b"),
                            ("KI19-15B", "ki19-15b"),
                            ("KI20-11B", "ki20-11b"),
                            ("KI20-12B", "ki20-12b"),
                        ],
                        default="NONE",
                        max_length=8,
                    ),
                ),
                ("IsMarried", models.BooleanField(default=False)),
            ],
        ),
    ]
