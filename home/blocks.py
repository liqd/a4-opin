from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.blocks import StructBlock, TextBlock, URLBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtaildocs.blocks import DocumentChooserBlock
from wagtail.wagtailembeds.blocks import EmbedBlock



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


COLOUR_CHOICES = (
    ("none", "none"), ("inverse", "inverse"), ("danger", "danger"))


class InfoBlock(blocks.StructBlock):

    background_colour = blocks.ChoiceBlock(
        choices=COLOUR_CHOICES, default="none", required=True)
    font_colour = blocks.ChoiceBlock(
        choices=COLOUR_CHOICES, default="black", required=True)
    heading = TextBlock()
    image = ImageChooserBlock(required=False)
    embedded_video = EmbedBlock(required=False)
    text = TextBlock()
    internal_link = URLBlock(required=False)

    class Meta:
        template = 'home/blocks/info_block.html'
        icon = 'glyphicon glyphicon-blackboard'
        label = 'Info Block'

class HeroUnitBlock(blocks.StructBlock):

    background_image = ImageChooserBlock()

    class Meta:
        template = 'home/blocks/hero_unit.html'
        icon = 'placeholder'
        label = 'Hero Unit'