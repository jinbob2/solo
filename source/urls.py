"""source URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url , include
from django.contrib import admin
from .views import Home
from .views import UsercreateView , UserCreateDoneView

from django.conf import settings
from django.conf.urls.static import url,static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Home.as_view()),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/register/$', UsercreateView.as_view(), name='register'),
    url(r'^accounts/register/done', UserCreateDoneView.as_view(), name='register_done' ),
    url(r'^bord/', include('bord.urls', namespace='bord')),
    url(r'^contact/', include('contact.urls', namespace='contact')),

]

if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
