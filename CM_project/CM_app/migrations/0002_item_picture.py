# Generated by Django 5.0.6 on 2024-05-29 19:48

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("CM_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="picture",
            field=models.ImageField(default=django.utils.timezone.now, upload_to=""),
            preserve_default=False,
        ),
    ]
