from django.contrib import admin
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from configuration.models import OrganisationSetup

class OrganisationSetUpAdmin(ModelAdmin):
    model = OrganisationSetup
    add_to_settings_menu = False
    menu_laber = "Organisation Setup"
    menu_icon = "info-circle"
    menu_order = 290
    exclude_from_explorer = False

modeladmin_register(OrganisationSetUpAdmin)