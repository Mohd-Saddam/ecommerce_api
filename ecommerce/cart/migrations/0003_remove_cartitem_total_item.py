# Generated by Django 4.2.1 on 2023-06-04 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_rename_cartitems_cartitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='total_item',
        ),
    ]
