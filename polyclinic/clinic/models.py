from django.db import models

NAME_MAX_LENGTH = 300

Sex = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
]


class Position(models.Model):
    code = models.CharField(max_length=8, primary_key=True)
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    compensation = models.FloatField()
    duties = models.CharField(max_length=NAME_MAX_LENGTH)
    requirements = models.CharField(max_length=NAME_MAX_LENGTH)


class Employee(models.Model):
    code = models.CharField(max_length=8, primary_key=True)
    fullname = models.CharField(max_length=NAME_MAX_LENGTH)
    birthday = models.DateField()

    sex = models.CharField(choices=Sex, max_length=20)
    address = models.CharField(max_length=NAME_MAX_LENGTH)
    phone_number = models.CharField(max_length=NAME_MAX_LENGTH)
    person_id = models.CharField(max_length=20)
    position_code = models.ForeignKey(Position, to_field='code', on_delete=models.deletion.SET_NULL, null=True)


class Drug(models.Model):
    code = models.CharField(max_length=8, primary_key=True)
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    treatment_indications = models.CharField(max_length=NAME_MAX_LENGTH)
    contraindications = models.CharField(max_length=NAME_MAX_LENGTH)

    PackageType = [
        ('Glass', 'Glass'),
        ('PlasticBox', 'PlasticBox'),
        ('Pills', 'Pills')
    ]

    package_type = models.CharField(choices=PackageType, max_length=20)
    price = models.FloatField()


class Illness(models.Model):
    code = models.CharField(max_length=8, primary_key=True)
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    symptom = models.CharField(max_length=NAME_MAX_LENGTH)
    duration = models.IntegerField(verbose_name='Duration in days')
    consequences = models.CharField(max_length=NAME_MAX_LENGTH)
    drug1_code = models.ForeignKey(Drug, to_field='code', on_delete=models.deletion.SET_NULL, null=True,
                                   related_name='smth1')
    drug2_code = models.ForeignKey(Drug, to_field='code', on_delete=models.deletion.SET_NULL, null=True,
                                   related_name='smth2')
    drug3_code = models.ForeignKey(Drug, to_field='code', on_delete=models.deletion.SET_NULL, null=True,
                                   related_name='smth3')


class Patient(models.Model):
    fullname = models.CharField(max_length=NAME_MAX_LENGTH)
    birthdate = models.DateField()
    sex = models.CharField(choices=Sex, max_length=NAME_MAX_LENGTH)
    address = models.CharField(max_length=NAME_MAX_LENGTH)
    phone_number = models.CharField(max_length=NAME_MAX_LENGTH)
    appointment_date = models.DateTimeField()
    illness_code = models.ForeignKey(Illness, to_field='code', on_delete=models.deletion.SET_NULL, null=True)
    employee_code = models.ForeignKey(Employee, to_field='code', on_delete=models.deletion.SET_NULL, null=True)


