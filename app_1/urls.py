from django.urls import path
from app_1 import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:slug>', views.red, name='redirect_url'),
]