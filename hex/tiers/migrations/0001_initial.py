# Generated by Django 4.0.5 on 2022-06-06 13:01

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import tiers.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to=tiers.models.tier_image_file_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png'])])),
                ('expiring_link_val', models.PositiveIntegerField(blank=True, null=True)),
                ('expiring_link', models.CharField(blank=True, max_length=255, null=True)),
                ('custom_expiring_link', models.CharField(blank=True, max_length=255, null=True)),
                ('custom_link_height', models.PositiveIntegerField(blank=True, null=True)),
                ('custom_link_width', models.PositiveIntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('custom_images', models.ManyToManyField(to='tiers.customimages')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
