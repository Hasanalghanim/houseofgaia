# Generated by Django 5.1.4 on 2025-06-18 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_landingpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='aboutPage', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AllBlogsPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='AllBlogsPage', max_length=100)),
            ],
        ),
    ]
