# Generated by Django 3.1.5 on 2021-01-04 22:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('alfieldmanager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 4, 22, 29, 59, 454374, tzinfo=utc)),
        ),
    ]
