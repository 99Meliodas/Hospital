from django.db import models
region = (
    ("1", "Bishkek"),
    ("2", "Osh city"),
    ("3", "Batken"),
    ("4", "Djalal-Abad"),
    ("5", "Naryn"),
    ("6", "Osh"),
    ("7", "Talas"),
    ("8", "Chui"),
    ("9", "IK")
)

type_hp = (
    ("1", "государственная"),
    ("2", "частная")
)

type_doctor = (
    ("1", "терапевт"),
    ("2", "хирург")
)

class Hospital(models.Model):
    okpo = models.IntegerField(unique=True)
    region = models.CharField(max_length=222, choices=region)
    employees = models.CharField(max_length=100)
    state_or_private = models.CharField(max_length=222, choices=type_hp)


    def __str__(self):
        return str(self.okpo)

    class Meta:
        verbose_name = 'Больница'
        verbose_name_plural = 'Больницы'
        ordering = ['okpo', ]




class Nurse(models.Model):
    full_name = models.CharField(max_length=222)
    pin_code = models.CharField(max_length=14)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=25)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Медсестра'
        verbose_name_plural = 'Медсестры'
        ordering = ['-id', ]

def nurse_choice():
    nurse = Nurse.objects.all()
    nm = 0
    n1 = 1
    for i in nurse:
        if n1 > i.id:
            nm = i.id
    return nm


class Doctor(models.Model):
    type_dr = models.CharField(max_length=222, choices=type_doctor)
    full_name = models.CharField(max_length=222)
    pin_code = models.CharField(max_length=14)
    age = models.IntegerField()
    experience = models.IntegerField()
    phone_number = models.CharField(max_length=25)
    nurse = models.OneToOneField(Nurse, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    def __str__(self):
        return self.type_dr

    class Meta:
        verbose_name = 'Доктор'
        verbose_name_plural = 'Доктора'
        ordering = ['-id', ]

class Patient(models.Model):
    full_name = models.CharField(max_length=222)
    pin_code = models.CharField(max_length=14)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=25)
    description = models.TextField()
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'
        ordering = ['-id', ]

class Chief_Physician(models.Model):
    hospital = models.OneToOneField(Hospital, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=222)
    pin_code = models.CharField(max_length=14)
    age = models.IntegerField()
    experience = models.IntegerField()
    phone_number = models.CharField(max_length=25)
    nurse = models.OneToOneField(Nurse, on_delete=models.CASCADE)
    doctor = models.OneToOneField(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'ГлавВрач'
        verbose_name_plural = 'ГлавВрачи'
        ordering = ['-id', ]















