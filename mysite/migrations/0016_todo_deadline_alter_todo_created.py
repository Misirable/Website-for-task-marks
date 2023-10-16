# Generated by Django 4.1.3 on 2022-11-10 05:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mysite", "0015_alter_todo_created"),
    ]

    operations = [
        migrations.AddField(
            model_name="todo",
            name="deadline",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 11, 11, 12, 43, 24, 640149), null=True
            ),
        ),
        migrations.AlterField(
            model_name="todo",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 11, 10, 12, 43, 24, 640149),
                verbose_name="Время создания",
            ),
        ),
    ]