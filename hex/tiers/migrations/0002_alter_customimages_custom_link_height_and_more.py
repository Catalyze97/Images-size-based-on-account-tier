# Generated by Django 4.0.5 on 2022-06-05 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customimages',
            name='custom_link_height',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='customimages',
            name='custom_link_width',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]