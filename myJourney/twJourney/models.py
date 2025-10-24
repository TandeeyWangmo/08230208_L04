from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    studentID = models.CharField(max_length=8)
    age = models.IntegerField()
    education = models.CharField(max_length=100)
    hobbies = models.TextField()
    future_goals = models.TextField()

    def __str__(self):
        return self.name


class Learning_Activity(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lab_title = models.CharField(max_length=100)
    description = models.TextField()
    completion_date = models.DateField()

    def __str__(self):
        return self.lab_title
