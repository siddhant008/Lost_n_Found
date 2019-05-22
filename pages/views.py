from django.shortcuts import render
from .models import *
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, "pages/home.html", {})


def contact(request):
    contacts = Contact(name=request.POST.get('name', False), email=request.POST.get('email', False),
                       message=request.POST.get('message', False))
    if not (contacts.name and contacts.email and contacts.email):
        return render(request, 'pages/contact.html', {})
    else:
        contacts.save()
        message = messages.success(request, 'Your feedback is on our way...!! :)')
        return render(request, 'pages/contact.html', {message: message})


def about(request):
    return render(request, "pages/about.html", {})
