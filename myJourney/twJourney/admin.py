from django.contrib import admin
from .models import Student, Learning_Activity

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'studentID', 'age', 'education')


@admin.register(Learning_Activity)
class LearningActivityAdmin(admin.ModelAdmin):
    list_display = ('lab_title', 'student', 'completion_date')
    list_filter = ('completion_date',)
