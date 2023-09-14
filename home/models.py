from django.db import models
from modelcluster.fields import ParentalKey
from wagtail import blocks
from wagtail.admin.panels import MultiFieldPanel, InlinePanel, FieldPanel
from wagtail.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock

from wagtail.models import Page, Orderable

from home.block import FoundingPartnerBlock, MissionVision, Adblock, WelcomeSectionBlock, AboutSectionBlock, \
    ServiceSectionBlock, TestimonialSectionBlock


class HomePage(Page):

    max_count = 1

    body = StreamField([
        ('welcome', WelcomeSectionBlock()),
        ('about', AboutSectionBlock()),
        ('services', ServiceSectionBlock()),
        ('testimonial', TestimonialSectionBlock()),
    ], use_json_field=True)

    content_panels = Page.content_panels+[
        MultiFieldPanel([
            InlinePanel('carousel', max_num=5, min_num=1, label="Carousel Image")], heading="Hero Section"), # noqa
        # MultiFieldPanel([
        #     InlinePanel('testimonial', max_num=4, min_num=1, label="Testimony")], heading="Testimonial Section"), # noqa
        FieldPanel("body"),
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
