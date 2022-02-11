# Generated by Django 4.0.1 on 2022-02-05 02:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("workspace", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Checklist",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("x", models.DecimalField(decimal_places=2, max_digits=100)),
                ("y", models.DecimalField(decimal_places=2, max_digits=100)),
                ("width", models.DecimalField(decimal_places=2, max_digits=100)),
                ("height", models.DecimalField(decimal_places=2, max_digits=100)),
                ("title", models.CharField(max_length=200)),
                ("collapsed", models.BooleanField()),
                (
                    "workspace_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="workspace.workspace",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="PostIt",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("x", models.DecimalField(decimal_places=2, max_digits=100)),
                ("y", models.DecimalField(decimal_places=2, max_digits=100)),
                ("width", models.DecimalField(decimal_places=2, max_digits=100)),
                ("height", models.DecimalField(decimal_places=2, max_digits=100)),
                ("content", models.CharField(max_length=200)),
                ("collapsed", models.BooleanField()),
                (
                    "workspace_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="workspace.workspace",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("x", models.DecimalField(decimal_places=2, max_digits=100)),
                ("y", models.DecimalField(decimal_places=2, max_digits=100)),
                ("width", models.DecimalField(decimal_places=2, max_digits=100)),
                ("height", models.DecimalField(decimal_places=2, max_digits=100)),
                ("url", models.URLField()),
                (
                    "workspace_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="workspace.workspace",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ChecklistItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.CharField(max_length=200)),
                ("is_checked", models.BooleanField()),
                (
                    "checklist_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="component.checklist",
                    ),
                ),
            ],
        ),
    ]
