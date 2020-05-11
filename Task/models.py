from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=50)
    done = models.BooleanField(default=False)

def __init__(self):
    return self.task + "" + str('done')