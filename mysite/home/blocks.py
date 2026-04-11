from wagtail.blocks import CharBlock, RichTextBlock, StructBlock, URLBlock


class ProjectCardBlock(StructBlock):
    title = CharBlock()
    description = RichTextBlock(features=["bold", "italic", "link"])
    tech_stack = CharBlock(
        help_text="e.g. Python, JS, Django, etc..."

    )

    repo_link = URLBlock(help_text="Link to the GitHub repo")

    deployed_link = URLBlock(
        required=False, help_text="Live link, if available")

    class Meta:
        icon = "code"
        template = "home/blocks/project_card_block.html"
