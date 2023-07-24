from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class InputValues(models.Model):
 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    input_values = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']


