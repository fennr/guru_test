# Generated by Django 4.1.2 on 2022-10-26 15:18

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_alter_city_name_alter_shop_closing_alter_shop_house_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.city'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='closing',
            field=models.TimeField(default=datetime.time(20, 0)),
        ),
        migrations.AlterField(
            model_name='shop',
            name='opening',
            field=models.TimeField(default=datetime.time(8, 0)),
        ),
        migrations.AlterField(
            model_name='shop',
            name='street',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.street'),
        ),
    ]
