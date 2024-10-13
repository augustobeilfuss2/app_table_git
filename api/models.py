from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Valores(models.Model):
     usuario = models.ForeignKey(User, related_name='value', on_delete=models.CASCADE)
     value = models.CharField(max_length=255)


class Registros(models.Model):
     user=models.ForeignKey(User, related_name='registros', on_delete=models.CASCADE)
     date=models.DateField()
     value=models.DecimalField(max_digits=6, decimal_places=2)
     description=models.CharField(max_length=30, blank=True)
     tags=models.CharField(max_length=25, default='default')


class Tag(models.Model):
     user=models.ForeignKey(User, related_name='tags', on_delete=models.CASCADE)
     tags=models.CharField(max_length=25, default='default')


     