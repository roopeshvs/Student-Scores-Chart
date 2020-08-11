from django.contrib import admin

# Register your models here.
from ScoresAPI.models import StudentModel, ScoreModel

admin.site.register(StudentModel)
admin.site.register(ScoreModel)