# Generated by Django 2.2.6 on 2019-12-17 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furnitureSet', '0004_auto_20191216_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='furnituresetmodel',
            name='roomType',
            field=models.TextField(default=None),
        ),
    ]
