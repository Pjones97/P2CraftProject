# Generated by Django 5.1.5 on 2025-04-23 17:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Media', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='profile_pics/')),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('liked_crafts', models.ManyToManyField(blank=True, related_name='liked_by', to='Media.craftideamodel')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_crafts', models.ManyToManyField(blank=True, related_name='created_by', to='Media.craftideamodel')),
            ],
        ),
    ]
