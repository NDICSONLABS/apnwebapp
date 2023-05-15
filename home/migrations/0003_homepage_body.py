# Generated by Django 4.2.1 on 2023-05-13 17:26

import content.blocks
from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField([('AboutSection', wagtail.blocks.StructBlock([('MissionVisionImage', wagtail.images.blocks.ImageChooserBlock(required=True)), ('FoundingPartner', wagtail.blocks.StructBlock([('full_names', wagtail.blocks.CharBlock(help_text="Enter Founding partner's name.", required=True)), ('partnership_type', wagtail.blocks.CharBlock(help_text='Partnership position/type.', required=True)), ('background', content.blocks.RichtextBlock()), ('twitter', wagtail.blocks.StructBlock([('button_page', wagtail.blocks.PageChooserBlock(help_text='If selected, this url will be used first', required=False)), ('button_url', wagtail.blocks.URLBlock(help_text='If added, this url will be used secondarily to the button page', required=False))])), ('facebook', wagtail.blocks.StructBlock([('button_page', wagtail.blocks.PageChooserBlock(help_text='If selected, this url will be used first', required=False)), ('button_url', wagtail.blocks.URLBlock(help_text='If added, this url will be used secondarily to the button page', required=False))])), ('instagram', wagtail.blocks.StructBlock([('button_page', wagtail.blocks.PageChooserBlock(help_text='If selected, this url will be used first', required=False)), ('button_url', wagtail.blocks.URLBlock(help_text='If added, this url will be used secondarily to the button page', required=False))]))])), ('Adblock', wagtail.blocks.StructBlock([('statement', content.blocks.RichtextBlock()), ('donation_link', wagtail.blocks.StructBlock([('button_page', wagtail.blocks.PageChooserBlock(help_text='If selected, this url will be used first', required=False)), ('button_url', wagtail.blocks.URLBlock(help_text='If added, this url will be used secondarily to the button page', required=False))])), ('volunteer_button', wagtail.blocks.StructBlock([('button_page', wagtail.blocks.PageChooserBlock(help_text='If selected, this url will be used first', required=False)), ('button_url', wagtail.blocks.URLBlock(help_text='If added, this url will be used secondarily to the button page', required=False))]))]))]))], default='', use_json_field=True),
            preserve_default=False,
        ),
    ]
