# Generated by Django 4.1 on 2022-08-18 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_repairs', '0005_alter_blogpost_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-id']},
        ),
    ]
