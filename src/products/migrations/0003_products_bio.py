# Generated by Django 3.2 on 2021-04-20 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210420_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='bio',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
