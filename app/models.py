from django.db import models

# Create your models here.
class cricket(models.Model):
    Team=models.CharField(max_length=100,primary_key=True)
    

class detial(models.Model):
    Team=models.ForeignKey(cricket,on_delete=models.CASCADE)
    Name=models.CharField(max_length=100)
    Age=models.IntegerField()
    Email=models.EmailField()


class access(models.Model):
    Name=models.ForeignKey(detial,on_delete=models.CASCADE)
    Wife=models.CharField(max_length=100)
    Child=models.IntegerField()
