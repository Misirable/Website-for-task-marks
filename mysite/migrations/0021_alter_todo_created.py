# Generated by Django 4.1.3 on 2022-11-10 16:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mysite", "0020_alter_todo_created"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 11, 10, 23, 19, 27, 385842),
                verbose_name="Время создания",
            ),
        ),
    ]