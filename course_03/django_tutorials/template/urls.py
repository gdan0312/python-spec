from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^echo/$', views.echo),
    url(r'^filters/$', views.filters),
    url(r'^extend/$', views.extend)
]
