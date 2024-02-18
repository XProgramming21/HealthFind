from django.contrib import admin
from django.urls import include, path

from api import views


urlpatterns = [

    path('login', views.loginAPIView),
]
