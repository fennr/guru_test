# Generated by Django 4.1.2 on 2022-10-26 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='shop',
            name='closing',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='shop',
            name='house',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='shop',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='shop',
            name='opening',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='street',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
