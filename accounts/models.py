from django.db import models

# Create your models here.


class User(models.Model):
    class Role(models.TextChoices):
        STUDENT = 'STUDENT', 'Student'
        TEACHER = 'TEACHER', 'Teacher'
        SCHOOL_ADMIN = 'SCHOOL_ADMIN', 'School Admin'


    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    matricule = models.CharField(max_length=200)
    role = models.CharField(max_length=20, choices=Role.choices)



