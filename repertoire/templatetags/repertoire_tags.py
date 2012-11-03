from django import template

register = template.Library()

@register.filter
def to_class_name(value):
	return value.__class__.__name__


@register.filter_function
def order_by(queryset, args):
    args = [x.strip() for x in args.split(',')]
    return queryset.order_by(*args)