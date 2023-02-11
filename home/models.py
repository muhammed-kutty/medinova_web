
from django.db import models

# Create your models here.


class Department(models.Model):
    dep_name=models.CharField(max_length=100)
    dep_description=models.TextField()

    def __str__(self) :
        return self.dep_name

class Team(models.Model):
    doc_name=models.CharField(max_length=255)
    doc_spec=models.TextField(max_length=255)
    dep_name=models.ForeignKey(Department,on_delete=models.CASCADE)
    doc_img=models.ImageField(upload_to='doctors')

    def __str__(self) :
        return 'Dr.'+ self.doc_name +' - (' + self.doc_spec +')'

class Appointment(models.Model):

    pet_name    =models.CharField(max_length=255)
    pet_phn =models.CharField(max_length=10)
    pet_Email   =models.EmailField()
    booking_date    =models.DateField()
    doc_name    =models.ForeignKey(Team, on_delete=models.CASCADE)
    booked_on   =models.DateField(auto_now=True)


class Message(models.Model):

    yor_name    =models.CharField(max_length=255)
    yor_phn =models.CharField(max_length=10)
    your_Email   =models.EmailField()
    subjects   =models.CharField(max_length=255)
    messsage = models.TextField()
   



