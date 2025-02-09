# from django.contrib import admin
from django.urls import path
from . import views


app_name = 'shop'
urlpatterns = [
    path('', views.index, name='index'),
    path('course/<int:course_id>', views.single_course, name='single_course'),
    path('course/<int:course_id>/edit', views.single_course_edit, name='single_course_edit'),
]
