# Generated by Django 3.2 on 2021-04-28 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_products_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='bio',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='products',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]