# Generated by Django 2.2.6 on 2019-12-16 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furnitureSet', '0003_furnitureimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='furnituresetmodel',
            name='description',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='furnituresetmodel',
            name='itemList',
            field=models.TextField(default=None),
        ),
    ]
