# Generated by Django 4.2.1 on 2023-06-04 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_productimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/category'),
        ),
    ]
