from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.models import Orderable
from wagtail.admin.panels import (
    FieldPanel,
    MultiFieldPanel,
    InlinePanel,
    FieldRowPanel
    )
from wagtail.fields import RichTextField
from wagtail.contrib.forms.models import (
    AbstractEmailForm,
    AbstractFormField
)

from home.models import HomePage


class FormField(AbstractFormField):
    page = ParentalKey(
        'ContactPage',
        on_delete=models.CASCADE,
        related_name='form_fields',
    )


class ContactPage(AbstractEmailForm):

    template = "forms/contact_page.html"
    # This is the default path.
    # If ignored, Wagtail adds _landing.html to your template name
    landing_page_template = "forms/contact_page_landing.html"

    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro'),
        InlinePanel('form_fields', label='Form Fields'),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel("subject"),
        ], heading="Email Settings"),
    ]


class HomePageCarousel(Orderable, models.Model):
    page = ParentalKey("home.HomePage", related_name="carousel")
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",

    )

    panels = [
        FieldPanel('title'),
        FieldPanel('sub_title'),
        FieldPanel('image'),
    ]

    class Meta(Orderable.Meta):
        verbose_name = "Home Page Carousel Slide"


class Testimonial(Orderable, models.Model):
    page = ParentalKey("home.HomePage", related_name="testimonial")
    # title = models.CharField(max_length=255, default="Testimonials"),
    testifiers_quote = models.TextField()
    testifiers_name = models.CharField(max_length=255)
    testifiers_title = models.CharField(max_length=255)
    testifiers_photo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",

    )

    def save(self, *args, **kwargs) -> None:
        self.page_id = HomePage.objects.live().all()[0].pk
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return "{}'s Testimony".format(self.testifiers_name)

    panels = [
        # FieldPanel('title'),
        MultiFieldPanel([
            FieldPanel('testifiers_name'),
            FieldPanel('testifiers_title'),
            FieldPanel('testifiers_photo'),
            FieldPanel('testifiers_quote'),
        ], heading="Testifier"),
    ]

    class Meta(Orderable.Meta):
        verbose_name = "Testimonials"
        verbose_name_plural = "Testimonials"
