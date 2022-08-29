from django.urls import path, include, re_path as url
from .views import *
from . import views

# 
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
urlpatterns = [
  # url('^', views.index, name="index")
  url('^$',TemplateView.as_view(template_name="OAuth.html")),
  url('logout/',LogoutView.as_view())
]
