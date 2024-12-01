from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.homepage , name='home' ),
    path('project/',views.project , name='project' ),

]