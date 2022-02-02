from django.contrib import admin

from .models import Employee, Position, Drug, Illness, Patient

admin.site.register(Employee)
admin.site.register(Position)
admin.site.register(Drug)
admin.site.register(Illness)
admin.site.register(Patient)

