# from django.db import models
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import MultiFieldPanel, InlinePanel, FieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail import blocks

from content.blocks import Adblock, FoundingPartnerBlock


class HomePage(Page):

    max_count = 1

    body = StreamField([
        (
            'AboutSection', blocks.StructBlock([
                    ("MissionVisionImage", ImageChooserBlock(required=True)),
                    ('FoundingPartner', FoundingPartnerBlock()),
                    ("Adblock", Adblock()),
                ])
        ),
        # (
        #     'Volunteer Section', blocks.StructBlock([
        #             ("Mission & Vision Image", ImageChooserBlock(required=True)),
        #             ('Founding Partner', FoundingPartnerBlock()),
        #             ("Ad block", Adblock())
        #         ])
        # ),
        # (
        #     'Volunteer Section', blocks.StructBlock([
        #             ("Mission & Vision Image", ImageChooserBlock(required=True)),
        #             ('Founding Partner', FoundingPartnerBlock()),
        #             ("Ad block", Adblock())
        #         ])
        # ),
    ], use_json_field=True)

    content_panels = Page.content_panels+[
        MultiFieldPanel([
            InlinePanel('carousel', max_num=5, min_num=1, label="Image")], heading="Hero Section"), # noqa
        MultiFieldPanel([
            InlinePanel('testimonial', max_num=4, min_num=1, label="Testimony")], heading="Testimonial Section"), # noqa
        FieldPanel("body"),
    ]
