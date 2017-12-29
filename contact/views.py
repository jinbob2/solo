from django.shortcuts import render
from django.views.generic import CreateView, TemplateView

# Create your views here.
from .models import Contact
from .forms import ContactForm

class ContactCreateView(CreateView):
    model = Contact
    template_name = 'base.html'
    success_url = '/contact/done'
    form_class = ContactForm

class ContactDoneView(TemplateView):
    template_name = 'contact_done.html'
