from django import template
from django.shortcuts import render
from django.template.loader import render_to_string
from wagtail.admin.templatetags.wagtailuserbar import get_page_instance

from config.models import SocialMediaSite, OrganisationSetup, PageButtons

register = template.Library()

is_page = lambda p, q: p == q


@register.simple_tag
def bg_color(page_type):
    bgcolor = "#2b0000"
    if is_page(page_type, "contact_form"):
        bgcolor = "#FFFFFF"
    return bgcolor


@register.simple_tag
def load_socials(*args, **kwargs):
    return SocialMediaSite.objects.all()


@register.simple_tag
def load_organisation_info(*args, **kwargs):
    organisation = OrganisationSetup.objects.all()[0]
    return organisation


@register.simple_tag
def load_donate_button(*args, **kwargs):
    return PageButtons.objects.filter(button_type="donate")[0]


@register.simple_tag
def load_directions_button(*args, **kwargs):
    return PageButtons.objects.filter(button_type="direction")[0]


@register.simple_tag
def load_button(btntype, *args, **kwargs):
    return PageButtons.objects.filter(button_type=btntype)[0]


@register.simple_tag
def check_pos(pos, value=None, *args, **kwargs):
    print("pos: ", pos)
    if not not value:
        print("from organisation_tag", "pos: ", pos, "value: ", value)
        return pos == value
    return pos != 1 and pos != 4


@register.simple_tag
def is_pos(item, item_list):
    return item_list.index(item) == 2


@register.simple_tag(takes_context=True)
def load_partnership_form(context, *args, **kwargs):
    template_name = ""
    page = context['page']
    page_type = page.page_type
    form = context['form']
    print('page', page, '\nform', context['csrf_token'])
    if is_page(page_type, "contact_form"):
        template_name = "home/sections/contact_section.html"
    elif is_page(page_type, "donation_form"):
        template_name = "home/sections/donate_section.html"
    else:
        template_name = "home/sections/volunteer_section.html"
    return render_to_string(template_name=template_name,
                            context=context.update(dict(page=page, form=form, csrf_token=context['csrf_token'])))
