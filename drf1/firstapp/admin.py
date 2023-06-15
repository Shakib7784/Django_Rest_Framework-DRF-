from django.contrib import admin
from firstapp.models import Student,Course
# Register your models here.

@admin.register(Student)
class StudentModel(admin.ModelAdmin):
    list_display=["id","name","roll"]
    
@admin.register(Course)
class CourseModel(admin.ModelAdmin):
    list_display=["course_id","name","mark","student"]