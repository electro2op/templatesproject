from django.contrib import admin
from django.urls import path
from inmakesapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home),
    path('about/', views.aboutus),
    path('login/', views.login),
    path('register/', views.register),
    path('contact/',views.contact),
    path('index/', views.index),
    path('index/opp/', views.operations, name='operations'),


]
