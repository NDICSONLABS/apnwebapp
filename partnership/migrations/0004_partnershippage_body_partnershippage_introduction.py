# Generated by Django 4.2.1 on 2023-09-12 18:15

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('partnership', '0003_partnershippage'),
    ]

    operations = [
        migrations.AddField(
            model_name='partnershippage',
            name='body',
            field=wagtail.fields.StreamField([('CTA', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('cta_button', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('pos', wagtail.blocks.IntegerBlock(max_value=4, min_value=1)), ('icon', wagtail.images.blocks.ImageChooserBlock(required=True)), ('action_name', wagtail.blocks.CharBlock(help_text="Enter intended action name .e.g. 'Make a Donation' ", required=True)), ('link_page', wagtail.blocks.PageChooserBlock(help_text='Selected the specific Page to go to', required=True))]), max_num=2, min_num=2))])))], default='', use_json_field=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='partnershippage',
            name='introduction',
            field=wagtail.fields.RichTextField(default='APN welcomes partners from different countries and ministries all over the world to support and facilitate the realization of its mission. Partnership is established by a longterm commitment to either financially support the mission, and/or volunteer skill/time for service. You can partner financially by subscribing for a periodic contribution and/or by volunteering your time and skills. '),
        ),
    ]