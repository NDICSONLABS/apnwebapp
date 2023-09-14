from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.models import Orderable


class PageButtons(models.Model):
    class ButtonType:
        DONATE = "donate"
        VOLUNTEER = "volunteer"
        DIRECTION = "direction"
        OTHER = "other"

        BUTTON_CHOICES = [
            (DONATE, "donate"),
            (DIRECTION, "direction"),
            (VOLUNTEER, "volunteer"),
            (OTHER, "other"),
        ]

    button_type = models.CharField(max_length=255, choices=ButtonType.BUTTON_CHOICES, help_text="Choose the Button type")

    link_page = models.ForeignKey(
        'wagtailcore.Page',
        verbose_name='link to an internal page',
        blank=True,
        null=True,
        related_name='+',
        on_delete=models.SET_NULL,
    )
    icon_name = models.CharField(
        verbose_name='icon class name',
        max_length=255,
        blank=True,
        null=True,
        default="gift"
    )
    link_text = models.CharField(
        verbose_name='link text',
        max_length=255,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.button_type

    class Meta:
        verbose_name='Page Button'
        verbose_name_plural='Page Buttons'


class OrganisationSetup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, blank=False, null=False, help_text="Name of Your Organistion")  # noqa
    abbreviation = models.CharField(max_length=150, blank=False, null=False,
                                    help_text="Abbreviated form of Your Organistion")  # noqa
    mission = models.TextField(blank=False, null=False, help_text="Your Organistion's Mission Statement")  # noqa
    vision = models.TextField(blank=False, null=False, help_text="Vison Statement for Your Organistion")  # noqa
    slogan = models.CharField(max_length=150, blank=False, null=False, help_text="Slogan of Your Organistion")  # noqa
    address = models.TextField(blank=False, null=False, help_text="Street, City, P.O. Box for Your Organistion")  # noqa
    phone = models.CharField(max_length=100, blank=False, null=False,
                             help_text="Telephone Number of Your Organistion")  # noqa
    email = models.CharField(max_length=255, blank=False, null=False,
                             help_text="Email Address of Your Organistion")  # noqa

    panels = [
        MultiFieldPanel([
            FieldPanel('name'),
            FieldPanel('abbreviation'),
            FieldPanel('mission'),
            FieldPanel('vision'),
            FieldPanel('slogan'),
        ], heading="Organisation's Details"),
        MultiFieldPanel([
            FieldPanel('phone'),
            FieldPanel('email'),
            FieldPanel('address'),
        ], heading="Address & Contact Information"),
    ]

    def __str__(self):
        return self.name


class SocialMediaSite(Orderable, models.Model):
    class Appellation:
        FACEBOOK = "twitter"
        TWITTER = "facebook"
        INSTAGRAM = "instagram"
        YOUTUBE = "youtube"
        WHATSAPP = "whatsapp"
        LINKEDIN = "linkedin"

        SITE_CHOICES = [
            (FACEBOOK, "twitter"),
            (TWITTER, "facebook"),
            (INSTAGRAM, "instagram"),
            (YOUTUBE, "youtube"),
            (WHATSAPP, "whatsapp"),
            (LINKEDIN, "linkedin"),
        ]

    name = models.CharField(max_length=255, choices=Appellation.SITE_CHOICES, help_text="Choose the media platform")
    link = models.URLField(blank=True, null=True, help_text="Your Organistion's Social link")  # noqa
    handle = models.CharField(max_length=255, blank=True, null=True,
                              help_text="Your Organistion's Social handle .e.g. @Agapepn")

    panels = [
        FieldPanel("name"),
        FieldPanel("link"),
        FieldPanel("handle"),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Social Media Link'
        verbose_name_plural = "Social Media Links"
