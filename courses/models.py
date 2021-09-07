from datetime import datetime

from django.db import models

class Speciality(models.Model):
    name = models.CharField(max_length=200)
    code = models.IntegerField(default=1)
    start_date = models.DateField(default=datetime.now())
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"

class Teacher(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Subject(models.Model):
    name = models.CharField(max_length=200)
    specialities = models.ForeignKey(Speciality, on_delete=models.CASCADE, related_name="subjects")
    teachers = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

class Test(models.Model):
    name = models.CharField(max_length=200)
    code = models.IntegerField(default=1)
