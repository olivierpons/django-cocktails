# Generated by Django 4.2.1 on 2023-05-21 11:14

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_populate"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="image",
            name="image",
        ),
        migrations.AddField(
            model_name="image",
            name="file",
            field=models.ImageField(
                blank=True, default=None, null=True, upload_to=main.models._path
            ),
        ),
        migrations.AlterField(
            model_name="image",
            name="title",
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]