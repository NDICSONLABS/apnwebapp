# Generated by Django 4.2.1 on 2023-09-13 12:13

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_homepage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField([('welcome', wagtail.blocks.StructBlock([('action_block', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('pos', wagtail.blocks.IntegerBlock(max_value=4, min_value=1)), ('icon', wagtail.images.blocks.ImageChooserBlock(required=True)), ('action_name', wagtail.blocks.CharBlock(help_text="Enter intended action name .e.g. 'Make a Donation' ", required=True)), ('link_page', wagtail.blocks.PageChooserBlock(help_text='Selected the specific Page to go to', required=False))]), max_num=4, min_num=0))])), ('about', wagtail.blocks.StructBlock([('mission_vision', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True))])), ('founding_partner', wagtail.blocks.StructBlock([('full_names', wagtail.blocks.CharBlock(help_text="Enter Founding partner's name.", required=True)), ('partnership_type', wagtail.blocks.CharBlock(help_text='Partnership position/type.', required=True)), ('background', wagtail.blocks.RichTextBlock(label='Background')), ('photo', wagtail.images.blocks.ImageChooserBlock(required=False)), ('twitter', wagtail.blocks.URLBlock(help_text='Enter your Twitter social media link')), ('facebook', wagtail.blocks.URLBlock(help_text='Enter your Facebook social media link')), ('instagram', wagtail.blocks.URLBlock(help_text='Enter your Instagram social media link'))])), ('ad_block', wagtail.blocks.StructBlock([('statement', wagtail.blocks.RichTextBlock(label='Statement'))]))])), ('services', wagtail.blocks.StructBlock([('section_title', wagtail.blocks.CharBlock(help_text='Enter a title.', required=True)), ('content', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.blocks.CharBlock(help_text='Enter a title.', required=True)), ('description', wagtail.blocks.RichTextBlock(help_text='Describe the service/project requiring funding.', label='Description')), ('campaign_page', wagtail.blocks.PageChooserBlock(help_text='Selected the specific donation Page', required=True))])))])), ('testimonial', wagtail.blocks.StructBlock([('section_title', wagtail.blocks.CharBlock(help_text='Enter a title.', required=True))]))], use_json_field=True),
        ),
    ]