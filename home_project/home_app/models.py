from django.db import models



class student(models.Model):
    name=models.CharField(max_length=20)
    roll=models.IntegerField()

    def __str__(self):
        return self.name
