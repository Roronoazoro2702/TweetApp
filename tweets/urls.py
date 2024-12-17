from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tweets/', views.tweet_list, name='tweet_list'),
]
