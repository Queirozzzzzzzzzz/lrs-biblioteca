# Generated by Django 4.2.5 on 2023-11-15 17:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="book",
            name="final_date",
        ),
        migrations.RemoveField(
            model_name="book",
            name="start_date",
        ),
        migrations.AddField(
            model_name="userloan",
            name="final_date",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="userloan",
            name="start_date",
            field=models.DateTimeField(
                auto_now_add=True, default="2023-11-15 12:00:00"
            ),
            preserve_default=False,
        ),
    ]
