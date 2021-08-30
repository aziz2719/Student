from django.db import models
from django.contrib.auth.models import AbstractUser

class Student(AbstractUser):
    first_name = models.CharField('Имя', max_length=255)
    last_name = models.CharField('Фамилия', max_length=255)
    age = models.PositiveIntegerField('Возраст', default=0)
    faculty = models.CharField('Факультет', max_length=255)
    direction = models.CharField('Направление', max_length=255)
    email = models.EmailField('Email адрес', null=True)
    phone = models.CharField('Номер телефона', max_length=30, blank=True)
        
    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return f'{self.username} {self.first_name} {self.last_name}'


class ImageStudent(models.Model):
    student = models.ForeignKey('users.Student', models.CASCADE, related_name='student_image', null=True)
    image = models.FileField('Фото', upload_to = 'student_images')