from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.blocks import PageChooserBlock

from blog.models import BlogPage
from home.blocks import ProjectCardBlock


class HomePage(Page):

    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Homepage image",
    )
    hero_text = models.CharField(
        blank=True,
        max_length=255, help_text="Write an introduction for the site"
    )
    hero_cta = models.CharField(
        blank=True,
        verbose_name="Hero CTA",
        max_length=255,
        help_text="Text to display on Call to Action",
    )
    hero_cta_link = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Hero CTA link",
        help_text="Choose a page to link to for the Call to Action",
    )

    intro = RichTextField(blank=True)
    about = RichTextField(blank=True)

    top_project_title = models.CharField(
        max_length=120,
        blank=True,
        help_text="Main title for the top project card"
    )

    top_project_text = models.TextField(
        blank=True,
        help_text="Short project description"
    )

    top_project_stack = models.TextField(
        blank=True,
        help_text="One technology per line, for example: Python then Django then PostgreSQL"
    )

    top_project_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Top project image"
    )

    top_project_gh = models.URLField(
        blank=True,
        verbose_name="Link to the GitHub repo"
    )

    top_project_dep = models.URLField(
        blank=True,
        verbose_name="Link to the deployed site"
    )

    featured_projects = StreamField(
        [("project", ProjectCardBlock())],
        blank=True,
        use_json_field=True,
        help_text="Use this section to showcase your projects"
    )

    featured_posts = StreamField(
        [("post", PageChooserBlock(page_type="blog.BlogPage"))],
        blank=True,
        use_json_field=True,
        help_text="Pivck blog posts to feature on the homepage.",
    )

    def get_context(self, request):
        context = super().get_context(request)
        latest = BlogPage.objects.live().order_by('-first_published_at').first()
        context['latest_blogpage'] = latest
        return context

    content_panels = Page.content_panels + [



        MultiFieldPanel(
            [
                FieldPanel("image"),
                FieldPanel("hero_text"),
                FieldPanel("hero_cta"),
                FieldPanel("hero_cta_link"),
            ],
            heading="Hero section",
        ),

        FieldPanel('intro'),
        FieldPanel('about'),

        MultiFieldPanel(
            [
                FieldPanel("top_project_title"),
                FieldPanel("top_project_text"),
                FieldPanel("top_project_stack"),
                FieldPanel("top_project_image"),
                FieldPanel("top_project_gh"),
                FieldPanel("top_project_dep"),
            ],
            heading="Top project section",
        ),

        FieldPanel("featured_projects"),


        FieldPanel("featured_posts"),



    ]
