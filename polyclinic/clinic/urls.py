from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('employment_department', views.employment_department, name='emp_dep'),
    path('employment_department/<str:position_code>', views.employment_department, name='emp_dep')
]