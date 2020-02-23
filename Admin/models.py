from django.db import models


# Create your models here.
class Admin(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    password = models.CharField(max_length=255)
    can_add = models.BooleanField()
    can_delete = models.BooleanField()

    def __str__(self):
        return self.name
