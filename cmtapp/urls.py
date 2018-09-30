from django.conf.urls import url
from . import views

from django.conf import settings
from django.conf.urls.static import static

# app_name = 'mainapp'

urlpatterns = [
    url(r'^$', views.list_cmts, name='list_cmts'),
    url(r'^edit/$', views.edit_cmt, name='edit_cmt'),
    url(r'^add/$', views.add_cmt, name='add_cmt'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
