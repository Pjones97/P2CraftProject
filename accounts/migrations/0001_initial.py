# Generated by Django 5.1.5 on 2025-02-01 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('year', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('director', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('rating', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
    ]
