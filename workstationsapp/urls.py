from django.conf.urls import url
from . import views

from django.conf import settings
from django.conf.urls.static import static

# app_name = 'mainapp'

urlpatterns = [
    url(r'^$', views.list_workstations, name='list_workstations'),
    url(r'^edit/$', views.edit_workstation, name='edit_workstation'),
    url(r'^add/$', views.add_workstation, name='add_workstation'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
