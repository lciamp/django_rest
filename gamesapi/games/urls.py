from django.conf.urls import url
from .views import game_list, game_detail

urlpatterns = [
    url(r'^games/$', game_list),
    url(r'^games/(?P<pk>[0-9]+)/$', game_detail),
]