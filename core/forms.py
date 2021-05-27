from .models import Application, Scheme
from django import forms

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['adhar_card', 'USN', 'college', 'course', 'caste', 'merit','college_id_card', 'certificate', 'income_certificates', 'marks_cards_10th']


class SchemeForm(forms.ModelForm):
    class Meta:
        model = Scheme
        fields = ['introduction', 'income_ceiling', 'value_of_scholarship', 'how_and_when_to_apply']

        widgets = {
          'introduction': forms.Textarea(attrs={'rows':4, 'cols':15}),
          'income_ceiling': forms.Textarea(attrs={'rows':4, 'cols':15}),
          'value_of_scholarship': forms.Textarea(attrs={'rows':4, 'cols':15}),
          'how_and_when_to_apply': forms.Textarea(attrs={'rows':4, 'cols':15}),
        }