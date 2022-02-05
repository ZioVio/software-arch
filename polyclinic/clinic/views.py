import json
from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
from clinic.models import Patient, Employee, Position
from clinic.utils import dict_from_queryset


def index(request):
    for p in list(Patient.objects.all()):
        print(p.fullname)
    return HttpResponse('Hello world')


def employment_department(request, position_code=None):
    print(position_code)
    positions = dict_from_queryset(
        Position.objects.all() if position_code is None else Position.objects.filter(code=position_code)
    )
    for p in positions:
        pos_employees = dict_from_queryset(Employee.objects.filter(position_code=p['code']))
        p['employees'] = pos_employees

    print(positions)  # dict of needed info
    context = {
        'positions': positions
    }

    return HttpResponse(render(request, 'clinic/epm_dep.html', context))

