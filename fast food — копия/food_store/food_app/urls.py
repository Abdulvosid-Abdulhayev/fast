from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('add_food_type/', views.add_food_type, name='add_food_type'),
    path('add_food/', views.add_food, name='add_food'),
    path('food/<int:food_id>/', views.food_detail, name='food_detail'),  
    path('profile/', views.profile, name='profile'),
]
