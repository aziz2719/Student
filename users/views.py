from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Student, ImageStudent
from .serializers import StudentSerializer, ImageStudentSerializer


class StudentView(ModelViewSet):
    queryset = Student.objects.prefetch_related('student_image')
    serializer_class = StudentSerializer
    lookup_field = 'pk'


class StudentImageView(ModelViewSet):
    queryset = ImageStudent.objects.all()
    serializer_class = ImageStudentSerializer
    lookup_field = 'pk'
