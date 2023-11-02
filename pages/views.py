from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def home(request):
    return render(request, 'pages/about.html')

def contact(request):
    form = ContactForm() # Created an instance of the ContactForm class
    return render(request, 'pages/contact.html', {
        'form': form
    })