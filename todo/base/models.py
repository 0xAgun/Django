from django.db import models
from django.contrib.auth.models import User
 
class Task(models.Model):
    # taking input username title and others 
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    driscp = models.TextField(null=True, blank=True)
    complt = models.BooleanField(default=False)
    create = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title #return the task title name

    class Meta:
        ordering = ['complt']

