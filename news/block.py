from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class ContentBlock(blocks.StructBlock):
    heading = blocks.CharBlock(max_length=150)
    sub_heading = blocks.CharBlock(required=False, max_length=150)
    text_content = blocks.RichTextBlock()
    thumbnail = ImageChooserBlock(required=False)

    class Meta:
        form_classname = 'Content Block'
        template = 'newsletter/content_block.html'
        icon = 'doc-empty'
