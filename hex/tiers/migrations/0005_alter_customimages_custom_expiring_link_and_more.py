# Generated by Django 4.0.4 on 2022-06-02 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiers', '0004_customimages_tier_custom_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customimages',
            name='custom_expiring_link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customimages',
            name='custom_link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customimages',
            name='custom_link_height',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customimages',
            name='custom_link_width',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customimages',
            name='expiring_link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customimages',
            name='expiring_link_val',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customimages',
            name='link_200px',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customimages',
            name='link_400px',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customimages',
            name='link_original',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]