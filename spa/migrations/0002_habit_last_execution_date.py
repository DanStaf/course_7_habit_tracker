# Generated by Django 4.2 on 2024-12-07 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='last_execution_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата последнего выполнения'),
        ),
    ]
