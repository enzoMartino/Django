# Generated by Django 2.0.2 on 2018-04-23 23:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_auto_20180424_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2018, 4, 23, 23, 21, 43, 825450, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2018, 4, 23, 23, 21, 43, 824449, tzinfo=utc)),
        ),
    ]
