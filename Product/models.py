from django.db import models
from Section.models import Section


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    img = models.BinaryField()
    cost = models.IntegerField()
    desc = models.TextField()
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
