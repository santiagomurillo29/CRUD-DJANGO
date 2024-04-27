from django.db import models

# Create your models here.
class Personas(models.Model):
    name = models.CharField(max_length = 30, null = True )
    age = models.CharField(max_length = 30, null = True)
    date = models.DateField(null= True, default= None)
    time = models.DateTimeField(null=True, default= None)
    update = models.DateTimeField(null=True, default= None)

    def __str__(self):
        return self.nombre