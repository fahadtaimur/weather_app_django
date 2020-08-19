from django.urls import path
from django.contrib.auth import urls
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("forecast/", views.forecast, name="forecast"),
]