# Generated by Django 4.2.1 on 2023-09-12 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partnership', '0004_partnershippage_body_partnershippage_introduction'),
    ]

    operations = [
        migrations.RenameField(
            model_name='partnershippage',
            old_name='introduction',
            new_name='intro',
        ),
        migrations.RemoveField(
            model_name='partnershippage',
            name='body',
        ),
    ]