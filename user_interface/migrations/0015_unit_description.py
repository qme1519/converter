# Generated by Django 3.0.7 on 2020-06-10 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_interface', '0014_auto_20200606_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
