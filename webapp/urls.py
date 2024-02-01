from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create_record/', views.create_record, name='create_record'),
    path('update_record/<str:pk>/', views.update_record, name='update_record'),
    path('delete_record/<str:pk>/', views.delete_record, name='delete_record'),
    path('view_record/<str:pk>/', views.view_record, name='view_record'),
    ]
