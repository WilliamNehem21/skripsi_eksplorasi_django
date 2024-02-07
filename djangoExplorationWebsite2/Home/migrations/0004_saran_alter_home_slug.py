# Generated by Django 4.2.9 on 2024-02-07 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Home", "0003_alter_home_slug"),
    ]

    operations = [
        migrations.CreateModel(
            name="Saran",
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
                ("email", models.EmailField(max_length=254)),
                ("saran", models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name="home",
            name="slug",
            field=models.SlugField(blank=True, editable=False),
        ),
    ]