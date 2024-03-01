# Generated by Django 4.2.9 on 2024-03-01 19:26

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_alter_image_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='order',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]
