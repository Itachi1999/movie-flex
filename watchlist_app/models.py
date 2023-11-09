from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    year = models.IntegerField()
    active = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.title
