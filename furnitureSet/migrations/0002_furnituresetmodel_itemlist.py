# Generated by Django 2.2.6 on 2019-10-29 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furnitureSet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='furnituresetmodel',
            name='itemList',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
