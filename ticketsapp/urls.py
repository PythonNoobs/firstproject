from django.conf.urls import url
from . import views

from django.conf import settings
from django.conf.urls.static import static

# app_name = 'mainapp'

urlpatterns = [
    url(r'^$', views.list_tickets, name='list_tickets'),
    url(r'^edit/$', views.edit_ticket, name='edit_ticket'),
    url(r'^add/$', views.add_ticket, name='add_ticket'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
