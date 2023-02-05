from django.db import models

# Create your models here.
class orderTable(models.Model):
    name=models.CharField(max_length=20)
    dob=models.CharField(max_length=20)
    age=models.PositiveIntegerField()
    gender=models.CharField(max_length=15)
    mobile=models.CharField(max_length=15)
    email=models.EmailField()
    address=models.TextField()
    dptmnt=models.CharField(max_length=20)
    course=models.CharField(max_length=20)
    purpose=models.CharField(max_length=20)
    materials=models.TextField()
    
    def __str__(self):
        return self.name
       
