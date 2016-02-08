from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.blocks import StructBlock
from wagtail.wagtailcore.blocks import TextBlock
from wagtail.wagtailcore.blocks import URLBlock
from wagtail.wagtailcore.blocks import CharBlock
from wagtail.wagtailcore.blocks import ChoiceBlock
from wagtail.wagtailcore.blocks import BooleanBlock
from wagtail.wagtailcore.blocks import PageChooserBlock
from wagtail.wagtailcore.blocks import RichTextBlock
from wagtail.wagtailcore.blocks import URLBlock
from wagtail.wagtailcore.blocks import ListBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtaildocs.blocks import DocumentChooserBlock
from wagtail.wagtailembeds.blocks import EmbedBlock

#import feedparser


class InlineImageBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    internal_link = PageChooserBlock(required=False)
    link_text = TextBlock(required=False)
    no_border = BooleanBlock(required=False)


class InlineImagesBlock(blocks.StructBlock):

    inline_images = ListBlock(InlineImageBlock())
    columns = ChoiceBlock(choices=[
        ('4', 'three columns'),
        ('6', 'two columns'),
    ], icon='cup', required=False, help_text='')

    class Meta:
        template = 'home/blocks/inline_images_block.html'
        icon = 'placeholder'
        label = 'Inline Images Block'


class CallToActionBlock(blocks.StructBlock):
    internal_link = PageChooserBlock(required=False)
    external_link = URLBlock(required=False)
    link_text = TextBlock(required=False)


class InfoBlock(blocks.StructBlock):

    title = CharBlock(classname="full title", required=False)
    image = ImageChooserBlock(required=False)
    text = TextBlock(required=False)
    button = CallToActionBlock(required=False)
    highlight = ChoiceBlock(choices=[
        ('', 'None'),
        ('highlight', 'Highlight'),
        ('boxed', 'Boxed'),
        ('boxed2', 'Boxed Variation'),
    ], icon='cup',
        required=False,
        help_text='How should this block be displayed?'
    )

    class Meta:
        template = 'home/blocks/info_block.html'
        icon = 'placeholder'
        label = 'Info Block'


class VideoBlock(blocks.StructBlock):

    title = CharBlock(classname="full title")
    video = EmbedBlock()

    class Meta:
        template = 'home/blocks/video_block.html'
        icon = 'placeholder'
        label = 'Video Block'


class NewsBlock(blocks.StructBlock):

    title = CharBlock(classname="full title")
    news = CharBlock(classname="full title")

    class Meta:
        template = 'home/blocks/news_block.html'
        icon = 'placeholder'
        label = 'News Block'


class WideImageBlock(blocks.StructBlock):

    image = ImageChooserBlock()

    class Meta:
        template = 'home/blocks/wide_image_block.html'
        icon = 'placeholder'
        label = 'Wide Image Block'


class ContactBlock(blocks.StructBlock):

    title = CharBlock(classname="full title")
    name_label = CharBlock(classname="full title")
    email_label = CharBlock(classname="full title")
    subject_label = CharBlock(classname="full title")
    message_label = CharBlock(classname="full title")
    submit_label = CharBlock(classname="full title")

    class Meta:
        template = 'home/blocks/contact_block.html'
        icon = 'placeholder'
        label = 'Contact Block'


class AccordionItemBlock(blocks.StructBlock):
    title = TextBlock(required=False)
    content = TextBlock(required=False)


class AccordionBlock(blocks.StructBlock):

    accordion_items = ListBlock(AccordionItemBlock())

    class Meta:
        template = 'home/blocks/accordion_block.html'
        icon = 'placeholder'
        label = 'Accordion Block'
