from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('list/', views.list),
	path('add/', views.add),
	path('add_form/', views.add_form),
]
