from django.urls import path

from . import views

app_name = 'acompany'

urlpatterns = [
    path('', views.index, name="index"),
]
