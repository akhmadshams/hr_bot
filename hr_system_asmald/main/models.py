from datetime import datetime, timedelta, date
from django.db import models


class Anketa(models.Model):
    full_name = models.CharField(max_length=255)
    b_date = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    education = models.CharField(max_length=255)
    old_work = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    additions = models.CharField(max_length=255, null=True)
    create_at = models.DateTimeField(blank=True)
    select = models.BooleanField(default=False, null=True)
    rezerv = models.BooleanField(default=False, null=True)

    @classmethod
    def get_selected_objects(cls):
        return cls.objects.filter(select=True)

    @classmethod
    def get_false(cls):
        return cls.objects.filter(select=False)

    @classmethod
    def get_rezerv_objects(cls):
        return cls.objects.filter(rezerv=True, select=True)

    class Meta:
        verbose_name_plural = "Anketa ma'lumotlari"


class Position(models.Model):
    position_name = models.CharField(max_length=255, verbose_name='Ish positsiyasi')

    def __str__(self):
        return self.position_name

    class Meta:
        verbose_name_plural = "Positsiya"



class Department(models.Model):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    department_name = models.CharField(max_length=255, verbose_name='Bolim nomi')

    def __str__(self):
        return self.department_name

    class Meta:
        verbose_name_plural = "Bo\'lim"


class Staff(models.Model):
    contract_id = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    b_date = models.DateField()
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=1000)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    gender = models.CharField(max_length=255)
    date_join = models.DateField(verbose_name="Ishga qabul qilingan sanasi")
    comment = models.TextField()
    status = models.BooleanField(default=True)

    @classmethod
    def get_true(cls):
        return cls.objects.filter(status=True)


    @classmethod
    def get_false(cls):
        return cls.objects.filter(status=False)


    @classmethod
    def get_birthdays_between_monday_and_sunday(cls, ):
        today = date.today()
        monday = today - timedelta(days=today.weekday())
        sunday = monday + timedelta(days=6)
        birthdays = cls.objects.filter(b_date__range=[monday, sunday])
        return birthdays

    def __str__(self):
        return f'{self.full_name}    |    {self.phone}     |  {self.b_date}'


    class Meta:
        verbose_name_plural = "Ishchilar"



class Users(models.Model):
    user_id = models.BigIntegerField(unique=True, default=1)
    name = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255, null=True)

    def __str__(self):
        if self.user_name:
            return f"Ismi {self.name}   |    User name {self.user_name}  "
        else:
            return f"Ismi {self.name}"

    class Meta:
        verbose_name_plural = "Telegram user"



class Work(models.Model):
    work_title = models.CharField(max_length=255)
    image = models.CharField(max_length=500)
    description = models.TextField()

    def __str__(self):
        return self.work_title

    class Meta:
        verbose_name_plural = "Bosh ish o'rinlari ruyxati"

from birthday import BirthdayField, BirthdayManager

class ToDo(models.Model):
    task = models.CharField(max_length=500)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.task



class ExecutionTime(models.Model):
    last_execution = models.DateTimeField()




