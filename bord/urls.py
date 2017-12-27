from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import url,static

from .views import (
    BordListView,
    BordDetailView,
    BordCreateView,
    BordUpdateView,
    BordDeleteView,
)

urlpatterns = [
    url(r'^$', BordListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', BordDetailView.as_view, name='detail'),
    url(r'^create/$', BordCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/update/$', BordUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', BordDeleteView.as_view(), name='delete'),
]