from django import template

register = template.Library()

@register.filter
def to_class_name(value):
	print "TO CLASS NAME VALUE IS %s" % value
	print value
	return value.__class__.__name__