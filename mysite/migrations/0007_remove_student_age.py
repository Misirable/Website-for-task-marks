# Generated by Django 4.1.3 on 2022-11-09 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mysite", "0006_alter_student_age_alter_student_name"),
    ]

    operations = [
        migrations.RemoveField(model_name="student", name="Age",),
    ]