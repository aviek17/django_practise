# Generated by Django 5.0 on 2023-12-26 16:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0002_rename_dodob_student_dob_alter_student_address"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="file",
            field=models.FileField(blank=True, null=True, upload_to=""),
        ),
        migrations.AlterField(
            model_name="student",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]