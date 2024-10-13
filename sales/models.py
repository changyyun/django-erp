from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField('date created')

    def __str__(self):
        return f"{self.name}, {self.date_created}"
