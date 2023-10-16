# Generated by Django 4.1.3 on 2022-11-09 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mysite", "0010_employee_delete_student"),
    ]

    operations = [
        migrations.CreateModel(
            name="ToDo",
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
                (
                    "title",
                    models.CharField(max_length=500, verbose_name="Название задания"),
                ),
                (
                    "is_complete",
                    models.BooleanField(default=False, verbose_name="Завершено"),
                ),
            ],
            options={"verbose_name": "Задание", "verbose_name_plural": "Задания",},
        ),
        migrations.DeleteModel(name="Employee",),
    ]
