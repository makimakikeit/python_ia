# Generated by Django 4.2.2 on 2023-06-20 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='release_date',
            field=models.DateField(blank=True, help_text='2022-01-31 のよう入力してください', null=True, verbose_name='発売日'),
        ),
    ]
