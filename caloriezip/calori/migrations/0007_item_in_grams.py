# Generated by Django 4.1.3 on 2022-11-06 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calori', '0006_alter_item_calories'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='in_grams',
            field=models.BooleanField(default=True),
        ),
    ]
