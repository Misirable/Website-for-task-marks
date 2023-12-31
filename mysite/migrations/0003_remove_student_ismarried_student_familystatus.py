# Generated by Django 4.1.3 on 2022-11-09 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mysite", "0002_alter_student_group_alter_student_sex"),
    ]

    operations = [
        migrations.RemoveField(model_name="student", name="IsMarried",),
        migrations.AddField(
            model_name="student",
            name="FamilyStatus",
            field=models.CharField(
                choices=[
                    ("-", "-"),
                    ("Состою в браке", "состою в браке"),
                    ("Не состою в браке", "не состою в браке"),
                ],
                default="-",
                max_length=17,
            ),
        ),
    ]
