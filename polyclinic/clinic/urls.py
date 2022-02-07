from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('employment_department', views.employment_department_handler, name='emp_dep'),
    path('employment_department/<str:position_code>', views.employment_department_handler, name='emp_dep'),
    path('illnesses/', views.illnesses_handler),
    path('illnesses_by_drugs/', views.illnesses_by_drugs_handler),
    path('patients', views.patients_handler),
    path('doctor_patients/<str:doctor_code>', views.doctor_patients_handler)
]