from django.db import models

# Create your models here.
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

class ExtendUser(models.Model):
    _id=models.OneToOneField(User,on_delete=CASCADE)
    phone = models.CharField(max_length=20)