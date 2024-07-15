from django.urls import path

from aclient import views

app_name = 'aclient'

urlpatterns = [
    path('', views.index, name="index"),
]
