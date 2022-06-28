from django.db import models
# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=85)
    phone=models.CharField(max_length=13)
    Desc=models.CharField(max_length=300)
    date=models.DateField(null=True)

    def __str__(self):
        return self.name 


