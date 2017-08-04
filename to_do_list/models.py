from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=40)


class Task(models.Model):
    text = models.CharField(max_length=200)
    deadline = models.DateTimeField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
