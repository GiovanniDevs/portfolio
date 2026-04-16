from wagtail import blocks


class CodeBlock(blocks.StructBlock):
    language = blocks.ChoiceBlock(
        choices=[
            ("python", "Python"),
            ("javascript", "JavaScript"),
            ("bash", "Bash"),
            ("html", "HTML"),
            ("css", "CSS"),
            ("json", "JSON"),
            ("sql", "SQL"),
        ],
        default="python",
        required=True,
    )
    code = blocks.TextBlock(required=True)

    class Meta:
        icon = "code"
        label = "Code block"
        template = "blog/blocks/code_block.html"
