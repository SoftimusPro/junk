# Generated by Django 4.1.7 on 2023-03-20 02:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventary', '0002_rename_brand_brands'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Brands',
            new_name='CarsBrands',
        ),
    ]
