# Generated by Django 4.0.1 on 2022-02-05 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("component", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="checklist",
            name="color",
            field=models.CharField(default="#baaf13", max_length=10),
        ),
        migrations.AddField(
            model_name="postit",
            name="color",
            field=models.CharField(default="#baaf13", max_length=10),
        ),
    ]
