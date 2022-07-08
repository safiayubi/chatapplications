from django.urls import path
from . import views
urlpatterns = [
    path('', views.user, name='user'),
    path('<str:room>/', views.userchat, name='userchat'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
     path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
    
]