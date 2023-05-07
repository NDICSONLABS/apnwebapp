from django.db import models
from wagtail.admin.panels import FieldPanel, StreamFieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page
from wagtail.snippets.models import register_snippet
from .blocks import ExternalLinkWithChildrenBlock, PageLinkWithChildrenBlock

class Navbar(models.Model):
    """
    Model that represents website navigation bars.  Can be modified through the
    snippets UI.
    """
    name = models.CharField(max_length=255)
    menu_items = StreamField([
        ('external_link', ExternalLinkWithChildrenBlock()),
        ('page_link', PageLinkWithChildrenBlock()),
        ], use_json_field=True)

    panels = [
        FieldPanel('name'),
        FieldPanel('menu_items')
    ]

    def __str__(self):
        return self.name

register_snippet(Navbar)


class PageWithNavbar(Page):
    navbar = models.ForeignKey(
        Navbar,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    content_panels=[
        FieldPanel('title'),
        FieldPanel('navbar')
    ]
