from django.urls import path, re_path

from . import views

urlpatterns=[
    path('', views.index),
    re_path(r'^(?P<input>[0-9]+)/$', views.angka),
    re_path(r'^(?P<input>[\w-]+)/$', views.slug),
]