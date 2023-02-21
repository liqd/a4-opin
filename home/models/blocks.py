from wagtail import blocks as core_blocks
from wagtail.embeds import blocks as embed_blocks
from wagtail.images import blocks as image_blocks
from wagtail.snippets import blocks as snippet_blocks

from .snippets import PageCollection
from .snippets import RSSImport


class RSSImportBlock(core_blocks.StructBlock):
    feed = snippet_blocks.SnippetChooserBlock(
        required=True, target_model=RSSImport)

    class Meta:
        template = 'home/blocks/rss_import_block.html'
        icon = 'snippet'
        label = 'RSS Import'


class PageCollectionBlock(core_blocks.StructBlock):
    page_collection = snippet_blocks.SnippetChooserBlock(
        required=False, target_model=PageCollection)

    class Meta:
        template = 'home/blocks/page_collection_block.html'
        icon = 'snippet'
        label = 'Page Collection'


# Sub blocks
class InlineImageBlock(core_blocks.StructBlock):
    image = image_blocks.ImageChooserBlock()
    internal_link = core_blocks.PageChooserBlock(required=False)
    external_link = core_blocks.URLBlock(required=False)
    link_text = core_blocks.TextBlock(required=False)


class CallToActionBlock(core_blocks.StructBlock):
    internal_link = core_blocks.PageChooserBlock(required=False)
    external_link = core_blocks.URLBlock(required=False)
    link_text = core_blocks.TextBlock(required=False)


class ImageTextCTABlock(core_blocks.StructBlock):
    title = core_blocks.CharBlock(classname="full title", required=False)
    image = image_blocks.ImageChooserBlock(required=False)
    text = core_blocks.RichTextBlock(required=False)
    button = CallToActionBlock(required=False)


class HighlightedImageTextCTABlock(core_blocks.StructBlock):
    title = core_blocks.CharBlock(classname="full title", required=False)
    text = core_blocks.RichTextBlock(required=False)
    button = CallToActionBlock(required=False)
    highlight = core_blocks.ChoiceBlock(choices=[
        ('highlight', 'Highlight (blue)'),
        ('highlight-purple', 'Highlight (purple)'),
        ('highlight-green', 'Highlight (green)')
    ], icon='cup',
        required=False,
        help_text='Choose background colour of block'
    )


class InlineImagesBlock(core_blocks.StructBlock):

    inline_images = core_blocks.ListBlock(InlineImageBlock())
    columns = core_blocks.ChoiceBlock(choices=[
        ('4', 'three columns'),
        ('6', 'two columns'),
    ], icon='cup', required=False, help_text='')

    class Meta:
        template = 'home/blocks/inline_images_block.html'
        icon = 'placeholder'
        label = 'Inline Images Block'


# single col with optional bg colour and formatting and allignment
class InfoBlock(core_blocks.StructBlock):

    title = core_blocks.CharBlock(classname="full title", required=False)
    image = image_blocks.ImageChooserBlock(required=False)
    text = core_blocks.RichTextBlock(required=False)
    button = CallToActionBlock(required=False)
    highlight = core_blocks.ChoiceBlock(choices=[
        ('', 'None'),
        ('highlight', 'Highlight (blue)'),
        ('boxed', 'Boxed'),
        ('boxed2', 'Boxed Variation'),
        ('highlight-purple', 'Highlight (purple)')
    ], icon='cup',
        required=False,
        help_text='How should this block be displayed?'
    )
    alignment = core_blocks.ChoiceBlock(
        choices=[
            ('vertical', 'vertical'),
            ('horizontal', 'horizontal'),
        ],
        icon='cup',
        default='vertical',
        help_text='How should the text and image be aligned?'
    )

    class Meta:
        template = 'home/blocks/info_block.html'
        icon = 'placeholder'
        label = 'Info Block'


# 3 coloumn block with optional image
class ColumnBlock(core_blocks.StructBlock):
    title_col1 = core_blocks.CharBlock(classname="full title", required=False)
    image_col1 = image_blocks.ImageChooserBlock(required=False)
    text_col1 = core_blocks.RichTextBlock(required=False)

    title_col2 = core_blocks.CharBlock(classname="full title", required=False)
    image_col2 = image_blocks.ImageChooserBlock(required=False)
    text_col2 = core_blocks.RichTextBlock(required=False)

    title_col3 = core_blocks.CharBlock(classname="full title", required=False)
    image_col3 = image_blocks.ImageChooserBlock(required=False)
    text_col3 = core_blocks.RichTextBlock(required=False)

    class Meta:
        template = 'home/blocks/column_block.html'
        icon = 'grip'
        label = 'Column Block'


# 4 col clickable tiles with option image and link
# adding in list ensures only 4 can be added
class TileLinkColumnBlock(core_blocks.StructBlock):
    title = core_blocks.CharBlock(classname="full title", required=False)
    sub_title = core_blocks.CharBlock(classname="subtitle title",
                                      required=False)
    title_col1 = core_blocks.CharBlock(classname="full title", required=False)
    image_col1 = image_blocks.ImageChooserBlock(required=False)
    text_col1 = core_blocks.RichTextBlock(required=False)
    internal_link_col1 = core_blocks.PageChooserBlock(required=False)
    external_link_col1 = core_blocks.URLBlock(required=False)

    title_col2 = core_blocks.CharBlock(classname="full title", required=False)
    image_col2 = image_blocks.ImageChooserBlock(required=False)
    text_col2 = core_blocks.RichTextBlock(required=False)
    internal_link_col2 = core_blocks.PageChooserBlock(required=False)
    external_link_col2 = core_blocks.URLBlock(required=False)

    title_col3 = core_blocks.CharBlock(classname="full title", required=False)
    image_col3 = image_blocks.ImageChooserBlock(required=False)
    text_col3 = core_blocks.RichTextBlock(required=False)
    internal_link_col3 = core_blocks.PageChooserBlock(required=False)
    external_link_col3 = core_blocks.URLBlock(required=False)

    title_col4 = core_blocks.CharBlock(classname="full title", required=False)
    image_col4 = image_blocks.ImageChooserBlock(required=False)
    text_col4 = core_blocks.RichTextBlock(required=False)
    internal_link_col4 = core_blocks.PageChooserBlock(required=False)
    external_link_col4 = core_blocks.URLBlock(required=False)

    class Meta:
        template = 'home/blocks/tile_column_block.html'
        icon = 'grip'
        label = 'Tile Column Block'


# 1-3 column block with an optional image and CTA
class ColumnCTABlock(core_blocks.StructBlock):
    title = core_blocks.CharBlock(classname="full title", required=False)
    column_count = core_blocks.ChoiceBlock(choices=[
        ('4', 'three columns'),
        ('6', 'two columns'),
        ('12', 'one column'),
    ], icon='cup', required=False, help_text='Only add this number of columns')
    column = core_blocks.ListBlock(ImageTextCTABlock())

    class Meta:
        template = 'home/blocks/column_cta_block.html'
        icon = 'grip'
        label = '1-3 Column CTA Block'


# 1- 2 column block with an optional bg colour and CTA
class HighlitedColumnBlock(core_blocks.StructBlock):
    column_count = core_blocks.ChoiceBlock(choices=[
        ('6', 'two columns'),
        ('12', 'one column'),
    ], icon='cup', required=False, help_text='Only add this number of columns')
    column = core_blocks.ListBlock(HighlightedImageTextCTABlock())

    class Meta:
        template = 'home/blocks/highlighted_column_block.html'
        icon = 'grip'
        label = '1-2 Highlighted Column CTA Block'


class VideoBlock(core_blocks.StructBlock):

    title = core_blocks.CharBlock(classname="full title", required=False)
    video = embed_blocks.EmbedBlock()

    class Meta:
        template = 'home/blocks/video_block.html'
        icon = 'placeholder'
        label = 'Video Block'


class NewsBlock(core_blocks.StructBlock):

    title = core_blocks.CharBlock(classname="full title")
    news = core_blocks.CharBlock(classname="full title")

    class Meta:
        template = 'home/blocks/news_block.html'
        icon = 'placeholder'
        label = 'News Block'


class WideImageBlock(core_blocks.StructBlock):

    image = image_blocks.ImageChooserBlock()

    class Meta:
        template = 'home/blocks/wide_image_block.html'
        icon = 'placeholder'
        label = 'Wide Image Block'


class ContactBlock(core_blocks.StructBlock):

    title = core_blocks.CharBlock(classname="full title")
    name_label = core_blocks.CharBlock(classname="full title")
    email_label = core_blocks.CharBlock(classname="full title")
    subject_label = core_blocks.CharBlock(classname="full title")
    message_label = core_blocks.CharBlock(classname="full title")
    submit_label = core_blocks.CharBlock(classname="full title")

    class Meta:
        template = 'home/blocks/contact_block.html'
        icon = 'placeholder'
        label = 'Contact Block'


class AccordionItemBlock(core_blocks.StructBlock):
    title = core_blocks.TextBlock(required=False)
    content = core_blocks.RichTextBlock(required=False)


class AccordionBlock(core_blocks.StructBlock):

    accordion_items = core_blocks.ListBlock(AccordionItemBlock())

    class Meta:
        template = 'home/blocks/accordion_block.html'
        icon = 'placeholder'
        label = 'Accordion Block'


class ImageTextItemBlock(core_blocks.StructBlock):
    image = image_blocks.ImageChooserBlock()
    text = core_blocks.TextBlock()


class ImageTextBlockList(core_blocks.StructBlock):

    imageTextBlockList = core_blocks.ListBlock(ImageTextItemBlock())

    class Meta:
        template = 'home/blocks/imageTextBlockList_block.html'
        icon = 'placeholder'
        label = 'Image Text Block'
