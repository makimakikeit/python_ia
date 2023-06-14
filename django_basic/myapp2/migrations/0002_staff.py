# Generated by Django 4.2.2 on 2023-06-14 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ビジネスネーム')),
                ('information', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp2.staffinformation', verbose_name='社員情報')),
            ],
        ),
    ]
