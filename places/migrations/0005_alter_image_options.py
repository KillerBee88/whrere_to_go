# Generated by Django 4.2.9 on 2024-02-27 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_alter_place_options_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'verbose_name': 'Фотография', 'verbose_name_plural': 'Фотографии'},
        ),
    ]
