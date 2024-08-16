from django.db import models
import uuid

class Account(models.Model):
    username = models.CharField(primary_key=True, max_length=64)
    password = models.CharField(max_length=64)
    email = models.CharField(max_length=512)
