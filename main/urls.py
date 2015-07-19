from django.conf.urls import include, url
from .views import (
    IndexView,
    LoginView,
    DashboardView,
)


urlpatterns = [    
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^login/$', LoginView.as_view(), name='login'),

    url(r'^dashboard/$', DashboardView.as_view(), name='dashboard'),
]