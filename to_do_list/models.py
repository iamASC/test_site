from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Task(models.Model):
    text = models.CharField(max_length=200)
    deadline = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.text
