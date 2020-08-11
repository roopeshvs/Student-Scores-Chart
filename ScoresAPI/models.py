from django.db import models
from django.conf import settings

class StudentModel(models.Model):
    student_id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=100)

class ScoreModel(models.Model):
    s_id = models.ForeignKey(StudentModel, related_name='scores', on_delete=models.CASCADE)
    marks = models.IntegerField()