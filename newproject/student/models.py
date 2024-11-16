from turtle import heading
from django.db import models
from librarian.models import book

# Create your models here.

class student(models.Model):
    name=models.CharField(max_length=12)
    age=models.IntegerField()
    gender=models.CharField(max_length=12,choices=[('m','male'),('f','female')])
    profilephoto=models.FileField(upload_to='media')
    address=models.TextField()
    username=models.CharField(max_length=12)
    password=models.CharField(max_length=12)

    def __str__(self):
        return self.name

class booking(models.Model):
    bookid=models.ForeignKey('librarian.book',on_delete=models.CASCADE) 
    studentid=models.ForeignKey(student,on_delete=models.CASCADE)
    booking_date=models.CharField(max_length=12)
    return_date=models.CharField(max_length=12)
    status=models.CharField(max_length=12,default="pending")

