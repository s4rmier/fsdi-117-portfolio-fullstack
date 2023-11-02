from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=225, widget=forms.TextInput(attrs={'placeholder':'Name'}))

    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'E-Mail'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Message'}))