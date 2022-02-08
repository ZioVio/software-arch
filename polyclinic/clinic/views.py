import json
from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound

# Create your views here.
from clinic.models import Patient, Employee, Position, Illness, Drug
from clinic.utils import dict_from_queryset


def index(request):
    return HttpResponse('Hello world')


def employment_department_handler(request, position_code=None):
    all_positions = Position.objects.all()
    positions = dict_from_queryset(
        Position.objects.all() if position_code is None else Position.objects.filter(code=position_code)
    )
    for p in positions:
        pos_employees = dict_from_queryset(Employee.objects.filter(position_code=p['code']))
        p['employees'] = pos_employees

    context = {
        'positions': positions,
        'all_positions': all_positions,
        'position_code': position_code,
    }

    return HttpResponse(render(request, 'clinic/epm_dep.html', context))


def illnesses_handler(request):
    illnesses = dict_from_queryset(Illness.objects.all())
    drugs = dict_from_queryset(Drug.objects.all())
    for drug in drugs:
        for il in illnesses:
            drug_code = drug['code']
            for drug_field in ['drug1_code_id', 'drug2_code_id', 'drug3_code_id']:
                if il[drug_field] == drug_code:
                    il[drug_field] = drug

    for il in illnesses:
        il['drugs'] = [
            il['drug1_code_id'],
            il['drug2_code_id'],
            il['drug3_code_id'],
        ]

    context = {
        'illnesses': illnesses,
    }

    return HttpResponse(render(request, 'clinic/illnesses.html', context))


def illnesses_by_drugs_handler(request):
    ill = dict_from_queryset(Illness.objects.all())
    drugs = dict_from_queryset(Drug.objects.all())
    for drug in drugs:
        for il in ill:
            drug_code = drug['code']
            for drug_field in ['drug1_code_id', 'drug2_code_id', 'drug3_code_id']:
                if il[drug_field] == drug_code:
                    if 'cures' not in drug:
                        drug['cures'] = []
                    drug['cures'].append(il)

    context = {
        'drugs': drugs,
    }

    return HttpResponse(render(request, 'clinic/illnesses.html', context))


def patients_handler(request):
    """List of patients with illness and doctor with button do get all doctors patients"""
    patients = dict_from_queryset(Patient.objects.all())
    for p in patients:
        p['doctor'] = dict_from_queryset(Employee.objects.filter(code=p['employee_code_id']))[0]
        p['illness'] = dict_from_queryset(Illness.objects.filter(code=p['illness_code_id']))[0]

    context = {
        'patients': patients,
    }
    return HttpResponse(render(request, 'clinic/patients.html', context))


def doctor_patients_handler(request, doctor_code=None):
    """List of patients with illness and doctor"""
    try:
        doctor = Employee.objects.get(pk=doctor_code)
    except Employee.DoesNotExist:
        return HttpResponseNotFound(f'Cannot find doctor with code:{doctor_code}')

    doctor_dict = doctor.__dict__
    doctor_dict['patients'] = dict_from_queryset(
        Patient.objects.filter(employee_code_id=doctor_dict['code'])
    )

    context = {
        'doctor': doctor_dict,
    }

    return HttpResponse(render(request, 'clinic/doctor.html', context))
