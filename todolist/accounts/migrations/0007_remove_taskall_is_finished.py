# Generated by Django 2.0.6 on 2018-06-10 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20180610_1852'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskall',
            name='is_finished',
        ),
    ]