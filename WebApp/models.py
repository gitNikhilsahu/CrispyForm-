from django.db import models

class Person(models.Model):
    Name = models.CharField(max_length=130)
    Email = models.EmailField(blank=True)
    Job_Title = models.CharField(max_length=30, blank=True)
    Biodata = models.TextField(blank=True)
