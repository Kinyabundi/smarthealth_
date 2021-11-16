from django.db import models
from django.contrib.auth.models import AbstractUser


gender_choices = (
    ('Male','Male'),
    ('Female','Female'),
    ('Others','Others')
)

# Create your models here.
class User(AbstractUser):
    date_of_birth = models.CharField(max_length=12,blank=True)
    phone = models.CharField(max_length=12, blank=True)
    gender = models.CharField( max_length=10,choices=gender_choices, blank=True)
    national_id = models.IntegerField(default=0)
    pass
