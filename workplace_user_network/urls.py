from django.urls import path

from . import views

app_name = 'workplace_user_network'

urlpatterns = [
    path('', views.index, name='index'),
    path('workplace_network/create', views.create, name='create'),
    path('workplace_network/store/', views.store, name='store'),
    path('workplace_network/<int:id>/detail/', views.detail, name='detail'),
    path('workplace_network/<int:id>/edit/', views.edit, name='edit'),
    path('workplace_network/<int:id>/update/', views.update, name='update'),
    path('workplace_network/<int:id>/delete/', views.delete, name='delete'),
]