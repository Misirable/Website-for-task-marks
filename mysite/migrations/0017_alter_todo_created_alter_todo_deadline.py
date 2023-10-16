# Generated by Django 4.1.3 on 2022-11-10 05:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mysite", "0016_todo_deadline_alter_todo_created"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 11, 10, 12, 44, 53, 35923),
                verbose_name="Время создания",
            ),
        ),
        migrations.AlterField(
            model_name="todo", name="deadline", field=models.DateTimeField(null=True),
        ),
    ]
