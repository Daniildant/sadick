from django.db import models

from markdownx.models import MarkdownxField
from django.contrib.flatpages.models import FlatPage

class Post(FlatPage):
    seo = models.CharField(blank=True, max_length=100)
    markdown = MarkdownxField(blank=True)
    thumbnail = models.ImageField(null = True, blank = True)
    category = models.ForeignKey('Category', related_name='pages', blank=True, null=True)


class Category(models.Model):
    name = models.CharField(blank=True, max_length=100)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.slug
