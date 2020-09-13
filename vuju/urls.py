from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.user_login, name='userlogin'),
    path('order', views.order, name='order'),
    path('received', views.received_order, name='receivedproduct'),
]