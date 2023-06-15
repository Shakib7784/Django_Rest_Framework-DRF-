from rest_framework import serializers
from firstapp.models import Student,Course

             
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

class StudentSerializer(serializers.ModelSerializer):
    # course = CourseSerializer(many=True) # we have to make reverse relationship with course table here
    # course = serializers.StringRelatedField(many=True)
    course = serializers.HyperlinkedIdentityField(
        many=True,
        read_only=True,
        view_name="course-detail"
     )
    class Meta:
        model = Student
        fields = "__all__"
        
        
# class StudentSerializer(serializers.ModelSerializer):
#     course = CourseSerializer(many=True) # we have to make reverse relationship with course table here

#     class Meta:
#         model = Student
#         fields = "__all__"

#     def create(self, validated_data):
#         courses_data = validated_data.pop('course')
#         student = super().create(validated_data)
#         self.create_courses(student, courses_data)
#         return student

#     def update(self, instance, validated_data):
#         courses_data = validated_data.pop('course', [])
#         instance = super().update(instance, validated_data)
#         instance.course.all().delete()  # Delete existing courses
#         self.create_courses(instance, courses_data)
#         return instance

#     def create_courses(self, student, courses_data):
#         for course_data in courses_data:
#             course_data['student'] = student  # Set the student object
#             Course.objects.create(**course_data)  # Create the Course object

