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


class ImageTextBlock(blocks.StructBlock):

    left_column = ImageChooserBlock()
    right_column = TextBlock()

    class Meta:
        template = 'home/blocks/m_t_block.html'
        icon = 'placeholder'
        label = 'Image Text Block'


class TextImageBlock(blocks.StructBlock):

    left_column = TextBlock()
    right_column = ImageChooserBlock()

    class Meta:
        template = 'home/blocks/m_t_block.html'
        icon = 'placeholder'
        label = 'Text Image Block'


class EmbedTextBlock(blocks.StructBlock):

    left_column = EmbedBlock()
    right_column = TextBlock()

    class Meta:
        template = 'home/blocks/m_t_block.html'
        icon = 'placeholder'
        label = 'Video Text Block'


class TextEmbedBlock(blocks.StructBlock):

    left_column = TextBlock()
    right_column = EmbedBlock()

    class Meta:
        template = 'home/blocks/m_t_block.html'
        icon = 'placeholder'
        label = 'Text Video Block'


class ThreeImagesBlock(blocks.StructBlock):

    left_image = ImageChooserBlock()
    left_image_text = TextBlock()
    middle_image = ImageChooserBlock()
    middle_image_text = TextBlock()
    right_image = ImageChooserBlock()
    right_image_text = TextBlock()
    circles = BooleanBlock()

    class Meta:
        template = 'home/blocks/3_im_block.html'
        icon = 'placeholder'
        label = 'Three Images Block'


class CollapsibleTextBlock(blocks.StructBlock):

    heading = TextBlock()
    text = TextBlock()

    class Meta:
        template = 'home/blocks/collaps_t_block.html'
        icon = 'arrows-up-down'
        label = 'Collapsible Text'


class CallToActionBlock(blocks.StructBlock):
    internal_link = PageChooserBlock(required=False)
    external_link = URLBlock(required=False)
    link_text = TextBlock(required=False)


class InfoBlock(blocks.StructBlock):

    title = CharBlock(classname="full title", required=False)
    image = ImageChooserBlock(required=False)
    text = TextBlock()
    button = CallToActionBlock(required=False)
    highlight = ChoiceBlock(choices=[
        ('', 'None'),
        ('highlight', 'Highlight'),
        ('boxed', 'Boxed'),
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
