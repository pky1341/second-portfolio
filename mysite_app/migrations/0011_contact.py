# Generated by Django 4.1.4 on 2023-01-03 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite_app', '0010_webtype_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('text_area', models.TextField()),
            ],
        ),
    ]
