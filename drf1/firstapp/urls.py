from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'students', views.StudentViewSEt)
router.register(r"coursename",views.CourseViewSEt)
urlpatterns = [
    # path("",views.StudentList.as_view()),
    # path("<int:pk>",views.StudentDetails.as_view()),
    # path("course",views.CourseList.as_view()),
    # path("course/<int:pk>",views.CourseDetails.as_view(),name="course_details"),
    # path("",include(router.urls))
]
urlpatterns += router.urls