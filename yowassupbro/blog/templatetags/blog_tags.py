from django import template
from django.db.models import Count

register = template.Library()

from ..models import Post

@register.simple_tag
def total_posts():
    return Post.publication.count()

@register.inclusion_tag('post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.publication.order_by('-published')[:count]
    return { 'latest_posts': latest_posts }

@register.assignment_tag
def get_most_commented_posts(count=5):
    return Post.publication.annotate(
            total_comments=Count('comments')
            ).order_by('-total_comments')[:count]
