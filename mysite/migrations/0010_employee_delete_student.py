# Generated by Django 4.1.3 on 2022-11-09 08:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("mysite", "0009_student_remove_studentmodel_group_delete_groupmodel_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                ("emp_name", models.CharField(max_length=200)),
                ("emp_email", models.EmailField(max_length=254)),
                ("emp_contact", models.CharField(max_length=20)),
                ("emp_role", models.CharField(max_length=200)),
                ("emp_salary", models.IntegerField()),
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
        migrations.DeleteModel(name="Student",),
    ]
