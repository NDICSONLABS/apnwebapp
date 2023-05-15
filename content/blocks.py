"""Streamfields live in here."""

from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.templatetags.wagtailcore_tags import richtext


class TitleAndTextBlock(blocks.StructBlock):
    """Title and text and nothing else."""

    title = blocks.CharBlock(required=True, help_text="Add your title")
    text = blocks.TextBlock(required=True, help_text="Add additional text")

    class Meta:  # noqa
        template = "components/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"


class CardBlock(blocks.StructBlock):
    """Cards with image and text and button(s)."""

    title = blocks.CharBlock(required=True, help_text="Add your title")

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.TextBlock(required=True, max_length=200)),
                ("button_page", blocks.PageChooserBlock(required=False)),
            ]
        )
    )

    class Meta:  # noqa
        template = "components/card_block.html"
        icon = "placeholder"
        label = "Our Services"


class RichtextBlock(blocks.RichTextBlock):
    """Richtext with all the features."""
    
    # def __init__(self, required=True, help_text=None, editor="default", features=None, max_length=None, validators=..., **kwargs):
    #     super().__init__(required, help_text, editor, features, max_length, validators, **kwargs)
    #     if not not kwargs:
    #         self.meta.label = kwargs['label']

    def get_api_representation(self, value, context=None):
        return richtext(value.source)

    class Meta:  # noqa
        template = "components/richtext_block.html"
        icon = "doc-full"
        label = "Full RichText"


class SimpleRichtextBlock(blocks.RichTextBlock):
    """Richtext without (limited) all the features."""

    def __init__(
        self, required=True, help_text=None, editor="default", features=None, **kwargs # noqa
    ):  # noqa
        super().__init__(**kwargs)
        self.features = ["bold", "italic", "link"]

    class Meta:  # noqa
        template = "components/richtext_block.html"
        icon = "edit"
        label = "Simple RichText"


class CTABlock(blocks.StructBlock):
    """A simple call to action section."""

    title = blocks.CharBlock(required=True, max_length=60)
    text = blocks.RichTextBlock(required=True, features=["bold", "italic"])
    button_page = blocks.PageChooserBlock(required=False)
    button_url = blocks.URLBlock(required=False)
    button_text = blocks.CharBlock(required=True, default='Learn More', max_length=40) # noqa

    class Meta:  # noqa
        template = "components/cta_block.html"
        icon = "placeholder"
        label = "Call to Action"


class LinkStructValue(blocks.StructValue):
    """Additional logic for our urls."""

    def url(self):
        button_page = self.get('button_page')
        button_url = self.get('button_url')
        if button_page:
            return button_page.url
        elif button_url:
            return button_url

        return None

    # def latest_posts(self):
    #     return BlogDetailPage.objects.live()[:3]


class ButtonBlock(blocks.StructBlock):
    """An external or internal URL."""
    def __init__(self, local_blocks=None, **kwargs):
        super().__init__(local_blocks, **kwargs)
        if not (not (kwargs)):
            self.meta.label = kwargs['label']

    button_page = blocks.PageChooserBlock(required=False, help_text='If selected, this url will be used first', label="Link to an internal page") # noqa
    button_url = blocks.URLBlock(required=False, help_text='If added, this url will be used secondarily to the button page', label="Link to an external web page") # noqa

    # def get_context(self, request, *args, **kwargs):
    #     context = super().get_context(request, *args, **kwargs)
    #     context['latest_posts'] = BlogDetailPage.objects.live().public()[:3]
    #     return context

    class Meta:  # noqa
        template = "components/button_block.html"
        icon = "placeholder"
        label = "Single Button"
        value_class = LinkStructValue


class Adblock(blocks.StructBlock):
    'Ad block on the home page'
    statement = RichtextBlock()
    donation_link = ButtonBlock(label="Donation Link")
    volunteer_button = blocks.PageChooserBlock(required=True, help_text='If selected, this url will be used first') # noqa

    class Meta:
        icon = "user"


class FoundingPartnerBlock(blocks.StructBlock):
    'Founding partner block on the home page'
    full_names = blocks.CharBlock(required=True, help_text="Enter Founding partner's name.") # noqa
    partnership_type = blocks.CharBlock(required=True, help_text="Partnership position/type.") # noqa
    background = RichtextBlock(label="Background")
    photo = ImageChooserBlock(required=False)
    twitter = blocks.URLBlock(help_text="Enter your Twitter social media link")
    facebook = blocks.URLBlock(help_text="Enter your Facebook social media link")
    instagram = blocks.URLBlock(help_text="Enter your Instagram social media link")

    class Meta:
        icon = "user"
