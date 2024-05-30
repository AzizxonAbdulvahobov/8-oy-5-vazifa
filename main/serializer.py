from rest_framework import serializers
from . import models
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Courses
        fields = '__all__'
        
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teachers
        fields = '__all__'
        
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Students
        fields = '__all__'
        