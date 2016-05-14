from django.conf.urls import url
from django.contrib import admin

from .views import (team_create, team_list, team_detail, team_update, team_delete)

urlpatterns = [
    url(r'^$', team_list),
    url(r'^create$', team_create),
    url(r'^(?P<id>\d+)/$', team_detail, name='detail'),
    url(r'^update$', team_update),
    url(r'^delete$', team_delete),
]
