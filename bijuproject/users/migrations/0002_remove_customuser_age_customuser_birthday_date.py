# Generated by Django 5.1.7 on 2025-03-21 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='age',
        ),
        migrations.AddField(
            model_name='customuser',
            name='birthday_date',
            field=models.DateField(default='2000-01-01'),
        ),
    ]
