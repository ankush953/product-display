# Generated by Django 2.1.7 on 2019-05-03 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='instock',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='ratings',
            field=models.IntegerField(default=0),
        ),
    ]
