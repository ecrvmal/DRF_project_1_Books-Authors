from django.db import models


# Create your models here.


class Painters(models.Model):
    username = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField()
    email = models.CharField(max_length=64)
