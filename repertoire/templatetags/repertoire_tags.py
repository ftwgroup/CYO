from django import template

register = template.Library()

@register.filter
def to_class_name(value):
	if value.__class__.__name__ == "Page":
		return "Content"
	return value.__class__.__name__

@register.filter
def print_model_fields(value):
	print value._meta.get_all_field_names()
	for rt in value.richtextcontent_set.all():
		print rt._meta.get_all_field_names()
		print rt.text
	print value.richtextcontent_set
	return value

@register.filter_function
def order_by(queryset, args):
    args = [x.strip() for x in args.split(',')]
    return queryset.order_by(*args)