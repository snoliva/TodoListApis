# Generated by Django 2.0.6 on 2018-06-10 23:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20180610_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskall',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
