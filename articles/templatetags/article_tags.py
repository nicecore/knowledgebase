from django import template

register = template.Library()

from ..models import Category


@register.simple_tag
def category_list():
    return Category.objects.all()


