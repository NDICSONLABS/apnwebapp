from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from content.models import Testimonial


class TestimonialAdmin(ModelAdmin):
    model = Testimonial
    add_to_settings_menu = False
    menu_laber = "Testimonials"
    menu_icon = "comment-add-reversed"
    menu_order = 292
    exclude_from_explorer = False


modeladmin_register(TestimonialAdmin)
