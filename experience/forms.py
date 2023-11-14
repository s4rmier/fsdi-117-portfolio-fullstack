from django import forms
from .models import Experience

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['entity', 'title', 'description', 'period', 'technologies']
        widgets = {
            'entity': forms.TextInput(attrs={'placeholder': 'School or Company'}),
            'title': forms.TextInput(attrs={'placeholder': 'Course or Position'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description'}),
            'period': forms.TextInput(attrs={'placeholder': 'Period'}),
        }
