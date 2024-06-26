from django.contrib import admin
#from django.urls import path, include
#from . import views

# urlpatterns = [
#     path('', views.index, name = 'index'),
#     #path('all_emp', views.all_emp, name = 'all_emp'),
#     path('view_all_emp/', views.all_emp, name='view_all_emp'),
#     path('add_emp', views.add_emp, name = 'add_emp'),
#     path('remove_emp/<int:emp_id>', views.remove_emp, name = 'remove_emp'),
#     path('filter_emp', views.filter_emp, name = 'filter_emp'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view_all_emp/', views.all_emp, name='view_all_emp'),
    path('add_emp/', views.add_emp, name='add_emp'),
    path('remove_emp/', views.remove_emp, name='remove_emp'),  # Pattern for removing without ID
    path('remove_emp/<int:emp_id>/', views.remove_emp, name='remove_emp_detail'),  # Pattern for removing with ID
    path('filter_emp/', views.filter_emp, name='filter_emp'),
]
