from django.urls import path

from . import views

app_name = 'workplace_user_network'

urlpatterns = [
    path('', views.index, name='index'),
]