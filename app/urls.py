from . import views

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',views.index,name="index"),
    path('view_employee',views.view_employee,name= "view_employee"),
    path('add_employee',views.add_employee,name="add_employee"),
    path('remove_employee',views.remove_employee,name="remove_employee"),
    path('remove_employee/<emp_id>',views.remove_employee,name = 'remove_employee'),
    path('filter_employee',views.filter_employee,name="filter_employee")
]