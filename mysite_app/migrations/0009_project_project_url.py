# Generated by Django 4.1.4 on 2022-12-29 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite_app', '0008_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
