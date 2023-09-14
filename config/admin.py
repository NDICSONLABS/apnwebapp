from django.contrib import admin

# Register your models here.
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register, ModelAdminGroup

from config.models import OrganisationSetup, SocialMediaSite, PageButtons
from home.models import Testimonial


class PageButtonsAdmin(ModelAdmin):
    model = PageButtons
    add_to_settings_menu = False
    menu_laber = "Page Button"
    menu_icon = "link"
    menu_order = 300
    add_to_settings_menu = True
    exclude_from_explorer = False


class OrganisationSetUpAdmin(ModelAdmin):
    model = OrganisationSetup
    add_to_settings_menu = False
    menu_laber = "Organisation Setup"
    menu_icon = "info-circle"
    menu_order = 000
    add_to_settings_menu = False
    exclude_from_explorer = False


class SocialMediaSite(ModelAdmin):
    model = SocialMediaSite
    menu_order = 100
    menu_label = "Social Media Sites"
    menu_icon = "site"
    add_to_settings_menu = False
    exclude_from_explorer = False


class OrganisationSetUpGroupAdmin(ModelAdminGroup):
    menu_label = "Organisation"
    menu_icon = "group"
    menu_order = 500
    items = (OrganisationSetUpAdmin, SocialMediaSite)


class TestimonialAdmin(ModelAdmin):
    model = Testimonial
    add_to_settings_menu = False
    menu_laber = "Testimonials"
    menu_icon = "comment-add-reversed"
    menu_order = 292
    exclude_from_explorer = False


modeladmin_register(TestimonialAdmin)
modeladmin_register(PageButtonsAdmin)

modeladmin_register(OrganisationSetUpGroupAdmin)
