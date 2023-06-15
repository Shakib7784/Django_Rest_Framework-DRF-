from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from firstapp.models import Student, Course
from firstapp.serializers import StudentSerializer,CourseSerializer
from rest_framework import generics, viewsets

# Create your views here
#we can use function based view or class based view. we will use class based view



# class StudentList(APIView):
#     def get(self, request):
#         students= Student.objects.all() # accessing all data of student model
#         serializer = StudentSerializer(students,many = True) #making api(convert complex data to json data) from Students data , here many = True means that this model can generate multiple instance
#         return Response(serializer.data)  
       

#     def post(self, request, format=None):
#         serializer= StudentSerializer(data = request.data) # here request.data Handles data.  Works for 'POST', 'PUT' and 'PATCH' methods.
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
# class StudentDetails(APIView):
    
#     def get_object(self, pk):
#         try:
#             return Student.objects.get(pk=pk)
#         except Student.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         student = self.get_object(pk)
#         serializer = StudentSerializer(student)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         student = self.get_object(pk)
#         serializer = StudentSerializer(student, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         student = self.get_object(pk)
#         student.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
    
    
    
    
    
#get, post
# class StudentList(generics.ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# #get,put,delete,patch
# class StudentDetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
    
    
    
    
# #get, post
# class CourseList(generics.ListCreateAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer

# #get,put,delete,patch
# class CourseDetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer
    
    
    
    
class StudentViewSEt(viewsets.ModelViewSet):
     queryset = Student.objects.all()
     serializer_class = StudentSerializer
     
class CourseViewSEt(viewsets.ModelViewSet):
     queryset = Course.objects.all()
     serializer_class = CourseSerializer