import json
from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
from clinic.models import Patient, Employee, Position, Illness, Drug
from clinic.utils import dict_from_queryset


def index(request):
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


def illnesses(request):
    ill = dict_from_queryset(Illness.objects.all())
    drugs = dict_from_queryset(Drug.objects.all())
    for drug in drugs:
        for il in ill:
            drug_code = drug['code']
            for drug_field in ['drug1_code_id', 'drug2_code_id', 'drug3_code_id']:
                if il[drug_field] == drug_code:
                    il[drug_field] = drug
    return HttpResponse(ill)


def illnesses_by_drugs(request):
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

    return HttpResponse(drugs)
