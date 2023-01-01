# Generated by Django 4.1.4 on 2022-12-28 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite_app', '0006_alter_about_little_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achivement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Years_of_Experiences', models.IntegerField(default=0)),
                ('Happy_Customers', models.IntegerField(default=0)),
                ('Project_Finished', models.IntegerField(default=0)),
                ('Digital_Awards', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('per_key', models.CharField(blank=True, max_length=200, null=True)),
                ('per_value', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]