from django.conf.urls import url 
from . import views 
 
urlpatterns = [ 
    url(r'^$', views.index),
    url(r'^new/$', views.new),
    url(r'^create/$', views.create),
    url(r'^comment/([0-9]{1,})/$', views.comment),
    url(r'^destroy/([0-9]{1,})/$', views.destroy),
    url(r'^delete/([0-9]{1,})/$', views.delete)
] 
