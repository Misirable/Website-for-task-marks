# Generated by Django 4.1.3 on 2022-11-09 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mysite", "0004_alter_student_age_alter_student_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student", name="Age", field=models.IntegerField(default=0),
        ),
    ]
