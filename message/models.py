from django.db import models

# Create your models here.
class Message(models.Model):
    nim = models.IntegerField(max_length=10,default="")
    name = models.CharField(max_length=200, default="")
    word = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.word