# Generated by Django 4.2.2 on 2023-06-16 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="order",
            field=models.IntegerField(default=1, verbose_name="並び順"),
            preserve_default=False,
        ),
    ]