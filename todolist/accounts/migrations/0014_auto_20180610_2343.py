# Generated by Django 2.0.6 on 2018-06-10 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20180610_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskall',
            name='created',
            field=models.DateField(auto_now=True),
        ),
    ]