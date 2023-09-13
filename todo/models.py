from django.db import models
from django.contrib.auth.models import User

class ToDo(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title