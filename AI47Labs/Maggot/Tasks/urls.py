from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name="home"),
    path('index/', views.index, name="index"),
    path('logout/', views.logout_view, name="logout"),
    path('update_task/<str:pk>/', views.updateTask, name= "update_task"),
    path('delete_task/<str:pk>/', views.deleteTask, name= "delete_task"),
]