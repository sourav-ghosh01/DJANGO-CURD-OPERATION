from django.db import models

# Create your models here.
class Student(models.Model):
      f_name=models.CharField(max_length=100)
      l_name=models.CharField(max_length=100)
      email=models.EmailField(max_length=200)
      address=models.TextField(max_length=500)
      phone=models.CharField(max_length=10)
    

    
