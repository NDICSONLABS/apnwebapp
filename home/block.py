from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class MissionVision(blocks.StructBlock):
    'Founding partner block on the home page'
    image = ImageChooserBlock(required=True)  # noqa

    class Meta:
        icon = "pick"
        template = 'home/sections/components/mission_vision.html'


class ActionBlock(blocks.StructBlock):
    pos = blocks.IntegerBlock(min_value=1, max_value=4)
    icon = ImageChooserBlock(required=True)
    action_name = blocks.CharBlock(required=True,
                                   help_text="Enter intended action name .e.g. 'Make a Donation' ")  # noqa
    link_page = blocks.PageChooserBlock(required=False, help_text='Selected the specific Page to go to')  # noqa

    class Meta:
        icon = "pick"


class CTABlock(blocks.StructBlock):
    cta_button = blocks.ListBlock(ActionBlock(), min_num=2, max_num=2)

    class Meta:  # noqa
        template = 'partnership/components/cta_button.html'
        icon = 'plus-inverse'
        label = 'CTA Section'


class WelcomeSectionBlock(blocks.StructBlock):
    action_block = blocks.ListBlock(ActionBlock(), min_num=0, max_num=4)

    class Meta:  # noqa
        template = 'home/sections/welcome_section.html'
        icon = 'list-ul'
        label = 'Welcome Section'


class FoundingPartnerBlock(blocks.StructBlock):
    'Founding partner block on the home page'
    full_names = blocks.CharBlock(required=True, help_text="Enter Founding partner's name.")  # noqa
    partnership_type = blocks.CharBlock(required=True, help_text="Partnership position/type.")  # noqa
    background = blocks.RichTextBlock(label="Background")
    photo = ImageChooserBlock(required=False)
    twitter = blocks.URLBlock(help_text="Enter your Twitter social media link")
    facebook = blocks.URLBlock(help_text="Enter your Facebook social media link")
    instagram = blocks.URLBlock(help_text="Enter your Instagram social media link")

    class Meta:
        icon = "user"
        template = 'home/sections/components/founding_partner.html'
        label = 'Founding Partner'


class Adblock(blocks.StructBlock):
    'Ad block on the home page'
    statement = blocks.RichTextBlock(label="Statement")

    class Meta:
        icon = "tag"
        template = 'home/sections/components/ad_block.html'
        label = 'Ads Section'


class AboutSectionBlock(blocks.StructBlock):
    mission_vision = MissionVision()
    founding_partner = FoundingPartnerBlock()
    ad_block = Adblock()

    class Meta:  # noqa
        template = 'home/sections/about_section.html'
        icon = 'list-ul'
        label = 'About Section'


class ServiceSummaryBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=False)
    title = blocks.CharBlock(required=True, help_text="Enter a title.")  # noqa
    description = blocks.RichTextBlock(label="Description", help_text="Describe the service/project requiring funding.")
    campaign_page = blocks.PageChooserBlock(required=True, help_text='Selected the specific donation Page')  # noqa

    class Meta:  # noqa
        template = 'home/sections/components/service_summary.html'
        icon = 'list-ul'
        label = 'Service Summary'


class ServiceSectionBlock(blocks.StructBlock):
    section_title = blocks.CharBlock(required=True, help_text="Enter a title.")  # noqa
    content = blocks.ListBlock(ServiceSummaryBlock())

    class Meta:  # noqa
        template = 'home/sections/services_section.html'
        icon = 'doc-full'
        label = 'Campaign Summary'


class TestimonialSectionBlock(blocks.StructBlock):
    section_title = blocks.CharBlock(required=True, help_text="Enter a title.")  # noqa

    def get_context(self, value, parent_context=None):
        context = super(TestimonialSectionBlock, self).get_context(value=value, parent_context=parent_context)
        print(context["page"])
        return context

    class Meta:  # noqa
        template = 'home/sections/testimonial_section.html'
        icon = 'openquote'
        label = 'Testimonials Section'
