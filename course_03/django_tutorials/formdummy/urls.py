from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^review/$', views.SchemaView.as_view())
]
