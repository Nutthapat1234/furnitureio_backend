# Generated by Django 2.2.6 on 2019-11-11 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20191111_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(default='Images/None/No-image.jpg', upload_to='Images/Product/'),
        ),
    ]
