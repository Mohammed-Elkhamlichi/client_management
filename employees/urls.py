from django.urls import path
from .views import (
    employees_list,
    employees_delete,
    employees_update,
    get_employee_info
)


app_name = 'employees'


urlpatterns = [
    path('list/', employees_list, name='employees_list'),
    path('delete/', employees_delete, name='employees_delete'),
    path('update/', employees_update, name='employees_update'),
    path('info/', get_employee_info, name='get_employee_info'),
]