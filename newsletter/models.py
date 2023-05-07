from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, StreamFieldPanel
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtailtrans.models import TranslatablePage
from .blocks import InlineImageBlock


class ArticlePage(TranslatablePage):
    intro = RichTextField(blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image', blank=True, null=True, on_delete=models.SET_NULL, related_name='+', verbose_name=_("Image")
    )
    featured = models.BooleanField(default=False)
    body = StreamField([
        ('paragraph', blocks.RichTextBlock()),
        ('image', InlineImageBlock()),
   ])

    content_panels = TranslatablePage.content_panels + [
        FieldPanel('intro'),
        FieldPanel('featured'),
        ImageChooserPanel('image'),
        StreamFieldPanel('body'),
   ]
