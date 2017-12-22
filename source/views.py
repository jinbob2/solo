from django.views.generic import View
from django.shortcuts import render
from django.views.generic import TemplateView , CreateView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy

class Home(View):
    def get(self, request ,*args, **kwargs):
        # context = {
        # }
        return render( request , "home.html", { } )

class Bord(View):
    def get(self, request,*args, **kwargs):
        return render( request,"bord.html" , {} )

class UsercreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')

class UserCreateDoneView(TemplateView):
    template_name = 'registration/register_done.html'