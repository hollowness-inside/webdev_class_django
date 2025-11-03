from django.db import models


class UserProfile(models.Model):
    name = models.CharField(max_length=30)
    clan = models.CharField(max_length=30)
    status = models.CharField(max_length=25)
    year = models.IntegerField()
