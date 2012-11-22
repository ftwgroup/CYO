from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe
from repertoire.models import Concert

class TinyMCEEditor(forms.Textarea):

    class Media:
        js = (
            settings.STATIC_URL+'js/jquery.js',
            settings.STATIC_URL+'js/tiny_mce/jscripts/tiny_mce/jquery.tinymce.js',
            )

    def render(self, name, value, attrs=None):
        rendered = super(TinyMCEEditor, self).render(name, value, attrs)
        return rendered + mark_safe(u'''<script type="text/javascript">
    jQuery('#id_%s').tinymce({
        script_url : '%sjs/tiny_mce/tiny_mce.js',
        mode : "none",
        theme : "advanced",
        language : "en",
        theme_advanced_toolbar_location : "top",
        theme_advanced_toolbar_align : "left",
        theme_advanced_statusbar_location : "bottom",
        theme_advanced_buttons1 : "fullscreen,|,formatselect,|,bold,italic,|,sub,sup,|,bullist,numlist,|,anchor,link,unlink,|,code",
        theme_advanced_buttons2 : "",
        theme_advanced_buttons3 : "",
        theme_advanced_toolbar_align : "left",
        theme_advanced_path : false,
        theme_advanced_blockformats : "p,h2,h3",
        theme_advanced_resizing : true,
        width:  '680',
        height: '300',
        content_css : "%scss/text.css",
        plugins : "fullscreen,paste",
        paste_auto_cleanup_on_paste : true,
        relative_urls : false
    });
    </script>''' % (name, settings.STATIC_URL, settings.STATIC_URL))

class ConcertForm(forms.ModelForm):
    class Meta:
        model = Concert
        widgets = {
            'description': TinyMCEEditor(),
            'abstract': TinyMCEEditor(),
        }

class UploadFileForm(forms.Form):
    file = forms.FileField()