from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from clinic.models import Patient


def index(request):
    for p in list(Patient.objects.all()):
        print(p.fullname)
    return HttpResponse('Hello world')
