#models.py
import os
from django.db import models

class JiraSoftware(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    url = models.URLField()
    repository_name = models.CharField(max_length=100)

class JiraSoftwareList(models.Model):
    title = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    url = models.URLField()
    action = models.CharField(max_length=100)
    no_of_entries = models.IntegerField()
    page_number = models.IntegerField()

class JiraSoftwareLogs(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    url = models.URLField()
    repository_name = models.CharField(max_length=100)
    action = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)