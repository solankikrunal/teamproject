from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/$', views.home),
    url(r'^login/$', views.login),
    url(r'^post/$', views.post),  
    
]