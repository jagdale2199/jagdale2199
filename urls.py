from django.contrib import admin
from django.urls import path , include
from .views import signup,login,authentication,homepage,user,index,pale

urlpatterns = [
    path('signup/', signup),
    path('login/',login,name='login'),
    path('homepage/<int:user>/', homepage,name='homepage'),
    path('auth/', authentication),
    path('user/', user),
    path('index/',index),
    path('pale/',pale ,name='pale')


]
