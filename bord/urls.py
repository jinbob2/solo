from django.conf.urls import url

from .views import (
    BordListView,
    BordDetailView,
    BordCreateView,
    BordUpdateView,
    BordDeleteView,
)

urlpatterns = [
    url(r'^check/(?P<check>\d+)/$', BordListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$',BordDetailView.as_view(), name='detail'),
    url(r'^create/(?P<check>\d+)/$',BordCreateView.as_view(), name='create'),
    url(r'^update/(?P<pk>\d+)/$',BordUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$',BordDeleteView.as_view(), name='delete'),
]