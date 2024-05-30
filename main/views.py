from django.shortcuts import render
from rest_framework import generics
from .models import Courses, Teachers, Students
from .serializer import CourseSerializer, TeacherSerializer, StudentSerializer
from rest_framework.permissions import IsAdminUser , IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly
# Create your views here.

class CoursesApiList(generics.ListCreateAPIView):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CourseApiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]



class TeachersApiList(generics.ListCreateAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAdminUser]


class teacherApiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAdminUser]

class StudentsApiList(generics.ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAdminUser]



class StudentApiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]




