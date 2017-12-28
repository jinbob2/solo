from django.shortcuts import render

# Create your views here.
from .models import Bord
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
)
from .forms import BordForm

class BordListView(ListView):
    model = Bord
    template_name = 'bord/bord_list.html'

    # def get_context_data(self, *args, **kwargs):
    #     context = super(BordListView,self).get_context_data(*args, **kwargs)
    #     context['all_count'] = Bord.objects.all().count()

class BordCreateView(CreateView):
    model = Bord
    template_name = 'bord/bord_create.html'
    form_class = BordForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()

        return super(BordCreateView, self).form_valid(form)

class BordUpdateView(UpdateView):
    model = Bord
    template_name = 'bord/bord_update.html'
    form_class = BordForm

class BordDetailView(DetailView):
    model = Bord
    template_name = 'bord/bord_detail.html'

    # def get_context_data(self, *args , **kwargs):
    #     context = super(BordDetailView, self).get_context_data(*args, **kwargs)
    #     return context

class BordDeleteView(DeleteView):
    model = Bord
    queryset = Bord.objects.all()
    success_url = '/bord/'
    template_name = 'bord/bord_delete.html'