from auditions.models import Audition, ParentalInfo, AuditionerBackground
from django import forms

class AuditionForm(forms.ModelForm):
    class Meta:
        model = Audition

class AuditionForm2(forms.ModelForm):
    class Meta:
        model = ParentalInfo
        exclude = ('audition',)

class AuditionForm3(forms.ModelForm):
    class Meta:
        model = AuditionerBackground
        exclude = ('audition',)