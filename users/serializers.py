from rest_framework import serializers
from .models import Student, ImageStudent


class ImageStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageStudent
        fields = ('__all__')


class StudentSerializer(serializers.ModelSerializer):
    student_image = ImageStudentSerializer(many=True, read_only=True)
    class Meta:
        model = Student
        fields = ('id', 'username', 'first_name', 'last_name', 'age', 'faculty', 'direction', 'email', 'phone', 'student_image')

