from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', 'results.views.team_list'),
    url(r'^create$', 'results.views.team_create'),
    url(r'^detail/$', 'results.views.team_detail'),
    url(r'^update$', 'results.views.team_update'),
    url(r'^delete$', 'results.views.team_delete'),
]
