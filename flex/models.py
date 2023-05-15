from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

# Create your models here.
class FlexPage(Page):
    template='flex/flex_page.html'
    # subtitle = models.CharField(max_length = 150, blank=True, null=True)
    

    content_panels = Page.content_panels + [
        # FieldPanel('subtitle'),
    ]
    class Meta:
        verbose_name = "Flex Page"
        verbose_name_plural = "Flex Page"
        