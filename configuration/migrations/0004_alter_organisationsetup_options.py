# Generated by Django 4.2.1 on 2023-05-08 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0003_alter_organisationsetup_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='organisationsetup',
            options={'verbose_name': 'Organisation Setup', 'verbose_name_plural': 'Organisation Setup'},
        ),
    ]
