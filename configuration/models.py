from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting


@register_setting
class OrganisationSetup(BaseSiteSetting):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 150, blank=False, null=False, help_text="Name of Your Organistion")    # noqa
    abbreviation = models.CharField(max_length = 150, blank=False, null=False, help_text="Abbreviated form of Your Organistion")    # noqa
    mission = models.TextField(blank=False, null=False, help_text="Your Organistion's Mission Statement")   # noqa
    vision = models.TextField(blank=False, null=False, help_text="Vison Statement for Your Organistion")    # noqa
    slogan = models.CharField(max_length = 150, blank=False, null=False, help_text="Slogan of Your Organistion")    # noqa
    address = models.TextField(blank=False, null=False, help_text="Street, City, P.O. Box for Your Organistion")    # noqa
    phone = models.CharField(max_length = 100, blank=False, null=False, help_text="Telephone Number of Your Organistion")   # noqa
    email = models.CharField(max_length = 255, blank=False, null=False, help_text="Email Address of Your Organistion")  # noqa
    facebook = models.URLField(max_length = 200, blank=True, null=True, help_text="Your Organistion's Facebook Page")   # noqa
    twitter = models.URLField(max_length = 200, blank=True, null=True, help_text="Your Organistion's Twitter Handle")   # noqa    
    youtube = models.URLField(max_length = 200, blank=True, null=True, help_text="Your Organistion's Youtube Chanel")   # noqa    
    instagram = models.URLField(max_length = 200, blank=True, null=True, help_text="Your Organistion's Instagram Account")  # noqa
    linkedin = models.URLField(max_length = 200, blank=True, null=True, help_text="Your Organistion's LinkedIn link")   # noqa    
    whatsapp = models.URLField(max_length = 200, blank=True, null=True, help_text="Your Organistion's WhatsApp Contact")    # noqa

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
        MultiFieldPanel([
            FieldPanel('facebook'),
            FieldPanel('twitter'),
            FieldPanel('youtube'),
            FieldPanel('instagram'),
            FieldPanel('linkedin'),
            FieldPanel('whatsapp'),
        ], heading="Social Media Links"),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Organisation Setup"
        verbose_name_plural = "Organisation Setup"
