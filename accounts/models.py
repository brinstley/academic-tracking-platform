from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        STUDENT = 'STUDENT', 'Student'
        TEACHER = 'TEACHER', 'Teacher'
        SCHOOL_ADMIN = 'SCHOOL_ADMIN', 'School Admin'

    email = models.EmailField(unique=True)
    matricule = models.CharField(max_length=200, blank=True)
    role = models.CharField(max_length=20, choices=Role.choices, blank=True)


    @property
    def is_teacher(self):
        return self.role == self.Role.TEACHER

    @property
    def is_student(self):
        return self.role == self.Role.STUDENT

    @property
    def is_school_admin(self):
        return self.role == self.Role.SCHOOL_ADMIN




