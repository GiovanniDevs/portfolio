from wagtail import hooks
from wagtail.admin.rich_text.editors.draftail import features as draftail_features
from wagtail.admin.rich_text.converters.html_to_contentstate import (
    InlineStyleElementHandler,
)


@hooks.register("register_rich_text_features")
def register_accent_text_feature(features):
    feature_name = "rt_accent"
    type_ = "RT_ACCENT"

    control = {
        "type": type_,
        "label": "A*",
        "description": "Accent color text",
        "style": {"color": "#d1944b"},
    }

    features.register_editor_plugin(
        "draftail",
        feature_name,
        draftail_features.InlineStyleFeature(control),
    )

    db_conversion = {
        "from_database_format": {
            "span.c-accent": InlineStyleElementHandler(type_),
        },
        "to_database_format": {
            "style_map": {
                type_: {
                    "element": "span",
                    "props": {"class": "c-accent"},
                }
            }
        },
    }

    features.register_converter_rule(
        "contentstate", feature_name, db_conversion)
