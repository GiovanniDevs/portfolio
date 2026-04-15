from django import template

from base.models import FooterText

from wagtail.models import Site

from django.db.models import Q
from wagtail.documents import get_document_model

register = template.Library()


@register.inclusion_tag("base/includes/footer_text.html", takes_context=True)
def get_footer_text(context):
    footer_text = context.get("footer_text", "")

    if not footer_text:
        instance = FooterText.objects.filter(live=True).first()
        footer_text = instance.body if instance else ""

    return {
        "footer_text": footer_text,
    }


@register.simple_tag(takes_context=True)
def get_site_root(context):
    return Site.find_for_request(context["request"]).root_page


@register.simple_tag
def get_latest_cv_document():
    Document = get_document_model()
    # Picks newest document whose title includes CV or Resume
    return (
        Document.objects.filter(
            Q(title__icontains="cv") | Q(title__icontains="resume")
        )
        .order_by("-id")
        .first()
    )
