from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Create your views here.
def home(request):
    return render(request, 'pages/about.html')

def contact(request):
    if request.method == "POST":
        # send email
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            email_from = form.cleaned_data['email']

            html = render_to_string("pages/email.html", request.POST)
            
            send_mail("Message from " + name, message, email_from, ['s4rmier@gmail.com'], html_message=html)

            return redirect('home')
    
    else:
        #send the html
        form = ContactForm() #Create an instance of the form

    return render(request, 'pages/contact.html', {
        'form': form
    })