# Generated by Django 4.1 on 2022-08-18 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_repairs', '0004_alter_blogpost_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-created_at']},
        ),
    ]
