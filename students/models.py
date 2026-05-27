from django.db import models
from django.urls import reverse

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20, unique=True, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True)
    career = models.CharField(max_length=150, blank=True)
    email = models.EmailField(unique=True)
    photo = models.ImageField(upload_to='students/', blank=True, null=True)
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse('student-detail', kwargs={'pk': self.pk})
