# Generated by Django 4.0.4 on 2022-06-02 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiers', '0002_alter_tier_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tier',
            name='image',
        ),
        migrations.RemoveField(
            model_name='tier',
            name='link',
        ),
    ]