from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.models import Page, Orderable
from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel, InlinePanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):

    content_panels = Page.content_panels+[
        MultiFieldPanel([
            InlinePanel('carousel', max_num=5, min_num=1, label="Image")], heading="Banner Section"),
    ]

class HomePageCarousel(Orderable):
    page = ParentalKey("home.HomePage", related_name="carousel")
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",

    )
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)

    panels = [
        FieldPanel('title'),
        FieldPanel('sub_title'),
        FieldPanel('image'),
    ]
