from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^topic_details/(?P<pk>\d+)/$', views.topic_details, name='topic_details')
]
