from django import template
from django.utils import timezone

register = template.Library()

@register.filter
def filter_start_time_greater_than(queryset, time):
    return queryset.filter(start_time__gt=time)
