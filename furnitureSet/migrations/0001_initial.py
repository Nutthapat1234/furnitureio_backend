# Generated by Django 2.2.6 on 2019-10-27 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FurnitureSetModel',
            fields=[
                ('furnitureSetCode', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('description', models.CharField(default=None, max_length=255)),
            ],
        ),
    ]
