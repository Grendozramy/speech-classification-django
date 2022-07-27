from django.urls import path

from . import views

app_name = 'tugas_2'

urlpatterns = [
    path('', views.index, name='index'),
]