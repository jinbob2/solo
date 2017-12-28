from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse

import json

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Bord
from .forms import BordForm
# Create your views here.

class BordListView(ListView):
    model = Bord
    template_name = 'bord/bord_list.html'
    paginate_by = 2

    def get_context_data(self, *args,  **kwargs):
        context = super(BordListView, self).get_context_data(**kwargs)
        check = self.kwargs.get('check')
        context['object_list'] = Bord.objects.filter(check = check)
        context['check'] = self.kwargs.get('check')
        return context


class BordDetailView(DetailView):
    model = Bord
    template_name = 'bord/bord_detail.html'

class BordCreateView(CreateView):
    model = Bord
    template_name = 'bord/bord_create.html'
    form_class = BordForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super(BordCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(BordCreateView, self).get_context_data(**kwargs)
        context['check'] = self.kwargs['check']
        return context

class BordUpdateView(UpdateView):
    model = Bord
    form_class = BordForm
    template_name = 'bord/bord_update.html'

class BordDeleteView(DeleteView):
    model = Bord
    template_name = 'bord/bord_delete_confirm.html'

    def delete(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        obj = Bord.objects.get(pk=pk)
        obj.delete()
        return HttpResponseRedirect(reverse('bord:list', kwargs={'check': obj.check}))

