# Generated by Django 4.1.3 on 2022-12-25 19:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ppsproj', '0005_alter_shoppingcart_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingcart',
            name='confirmedTime',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='shoppingcart',
            name='creatingTime',
            field=models.DateField(default=datetime.date(2022, 12, 25)),
        ),
    ]
