from django.db import models
from django.shortcuts import render
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel


# Create your models here.


class FlexPage(RoutablePageMixin, Page):
    template = 'flex/flex_page.html'
    # subtitle = models.CharField(max_length = 150, blank=True, null=True)

    content_panels = Page.content_panels + [
        # FieldPanel('subtitle'),
    ]

    class Meta:
        verbose_name = "Service Page"
        verbose_name_plural = "Service Page"

    route(r"^flex")

    def get_services(self, request, *args, **kwargs):
        context = self.get_context(request, *args, **kwargs)
        return render(request, "flex/flex.html", context)

    def get_context_data(self, **kwargs):
        context = super(FlexPage, self).get_context_data(**kwargs)
        return context
