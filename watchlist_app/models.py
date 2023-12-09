from django.db import models

# Create your models here.
class StreamingPlatform(models.Model):
    name = models.CharField(max_length=50)
    about = models.CharField(max_length= 200)
    website = models.URLField(max_length=100)
    
    def __str__(self) -> str:
        return self.name

class DigitalContent(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    createdAt = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    platform = models.ForeignKey(StreamingPlatform, on_delete=models.CASCADE, related_name='digital_content')
    
    def __str__(self) -> str:
        return self.title
