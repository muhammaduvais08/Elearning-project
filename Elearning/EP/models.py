from django.db import models

# Create your models here.


# Model created
class student( models.Model ):
    Firstname = models.CharField(max_length=60)
    Lastname = models.CharField(max_length=60)
    Email = models.EmailField(max_length=60)
    Contact = models.BigIntegerField()
    
    
    def __str__( self ):
        return self.Firstname
    