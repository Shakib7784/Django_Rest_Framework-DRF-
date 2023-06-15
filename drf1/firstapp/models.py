from django.db import models

# Create your models here.


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    roll = models.IntegerField()
    def __str__(self) :
        return self.name
    
      
class Course(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name="course")
    course_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    mark = models.IntegerField()
    
    def __str__(self) :
        return f"{self.name}: {self.mark}"