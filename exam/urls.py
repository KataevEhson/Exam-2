from django.urls import path, include
from .views import *


urlpatterns = [
    path("", registration, name="registration"),
    path("login/", login_user, name="login"),
    path('create_stadium', create_stadium, name='create_stadium'),
    path('show_stadiums', show_stadiums, name='show_stadiums'),
]
