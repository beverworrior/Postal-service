from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_parcel, name='add_parcel'),
    path('edit/<int:pk>/', views.edit_parcel, name='edit_parcel'),
    path('delete/<int:pk>/', views.delete_parcel, name='delete_parcel'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]