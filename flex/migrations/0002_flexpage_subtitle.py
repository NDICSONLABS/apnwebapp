# Generated by Django 4.2.1 on 2023-05-09 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flexpage',
            name='subtitle',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]