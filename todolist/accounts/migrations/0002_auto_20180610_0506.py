# Generated by Django 2.0.6 on 2018-06-10 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskall',
            name='finished',
            field=models.DateField(null=True),
        ),
    ]