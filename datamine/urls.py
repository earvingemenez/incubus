from django.conf.urls import include, url
from .views import (
    CreateMineView,
    MineHomeView,
    DataListView,
)


urlpatterns = [
    url(r'^create/$', CreateMineView.as_view(), name='mine_create'),
    url(r'^(?P<mine_id>\d+)/$', MineHomeView.as_view(), name='mine_home'),
    url(r'^(?P<mine_id>\d+)/data/$', DataListView.as_view(), name='mine_datalist'),

]