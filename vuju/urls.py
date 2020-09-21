from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.user_login, name='userlogin'),
    path('all_users', views.get_all_users, name='allusers'),
    path('order', views.order, name='order'),
    path('received', views.received_order, name='receivedproduct'),
    path('songs/upcoming', views.get_upcoming_songs, name='upcomingsongs'),
    path('songs/request', views.request_song, name='requestsong'),
]