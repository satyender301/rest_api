from django.db import models



class Student(models.Model):
    firstname= models.CharField(max_length=60)
    lastname= models.CharField(max_length=60)

    def __str__(self):
        return self.firstname

