from django.urls import path

from . import views

urlpatterns = [
    path('add', views.FeedbackCreateView.as_view(), name='feedback-create'),
    path('', views.FeedbackCreateView.as_view(), name='feedback-list')
]
