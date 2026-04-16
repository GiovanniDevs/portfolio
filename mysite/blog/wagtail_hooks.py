from wagtail import hooks
from wagtail.admin.rich_text.editors.draftail import features as draftail_features
from wagtail.admin.rich_text.converters.html_to_contentstate import (
    InlineStyleElementHandler,
)


@hooks.register("register_rich_text_features")
def register_red_colour_feature(features):

    feature_name = "colour-red"
    type_ = "COLOUR_RED"

    control = {
        "type": type_,
        "label": "Red",
        "description": "Red emphasis text",
        "style": {"color": "#e53e3e"},
    }

    features.register_editor_plugin(
        "draftail",
        feature_name,
        draftail_features.InlineStyleFeature(control),
    )

    db_conversion = {
        "from_database_format": {
            "span.rt-red": InlineStyleElementHandler(type_),
        },
        "to_database_format": {
            "style_map": {
                type_: {
                    "element": "span",
                    "props": {"class": "rt-red"},
                }
            }
        },
    }

    features.register_converter_rule(
        "contentstate", feature_name, db_conversion)

# Make the feature available in rich text editors by default.
    if feature_name not in features.default_features:
        features.default_features.append(feature_name)
