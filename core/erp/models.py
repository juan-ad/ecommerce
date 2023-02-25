from django.db import models
from datetime import datetime

# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    
    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Tipo'
        db_table = 'tipo'


class Employee(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    names = models.CharField(max_length=150, verbose_name='Nombres')
    dni = models.CharField(max_length=10, unique=True, verbose_name='Dni')
    dateJoined = models.DateField(default=datetime.now, verbose_name='Fecha de registro')
    dateCreation = models.DateTimeField(auto_now=True)
    salary = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', null=True)

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Emleado'
        db_table = 'empleado'