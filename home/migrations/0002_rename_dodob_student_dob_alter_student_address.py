# Generated by Django 5.0 on 2023-12-26 11:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="student",
            old_name="DOdob",
            new_name="dob",
        ),
        migrations.AlterField(
            model_name="student",
            name="address",
            field=models.TextField(blank=True, null=True),
        ),
    ]
