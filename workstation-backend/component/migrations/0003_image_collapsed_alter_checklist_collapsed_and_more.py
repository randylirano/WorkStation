# Generated by Django 4.0.1 on 2022-02-09 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("component", "0002_checklist_color_postit_color"),
    ]

    operations = [
        migrations.AddField(
            model_name="image",
            name="collapsed",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="checklist",
            name="collapsed",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="postit",
            name="collapsed",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="postit",
            name="content",
            field=models.TextField(),
        ),
    ]
