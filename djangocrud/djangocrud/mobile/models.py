from django.db import models  
class Phone(models.Model):  
    phone_name = models.CharField(max_length=100)  
    phone_model = models.CharField(max_length=100)  
    make = models.IntegerField()  
    class Meta:  
        db_table = "phone"  