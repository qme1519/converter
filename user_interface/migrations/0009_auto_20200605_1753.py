# Generated by Django 3.0.7 on 2020-06-05 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_interface', '0008_auto_20200605_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updatecurrency',
            name='timestamp',
            field=models.BigIntegerField(),
        ),
    ]