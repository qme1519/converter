# Generated by Django 3.0.7 on 2020-06-06 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_interface', '0013_history'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='destination_value',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='history',
            name='source_value',
            field=models.CharField(max_length=200),
        ),
    ]
