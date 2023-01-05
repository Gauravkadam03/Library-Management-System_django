from django.db import models

# Create your models here.

class book(models.Model):
    B_name=models.CharField(max_length=60)
    A_name=models.CharField(max_length=25)
    Date=models.DateField()
    B_category=models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.B_name 