from distutils.command.upload import upload
from pyexpat import model
from django.db import models


class PDF(models.Model):
    name = models.CharField(max_length=255)
    thumb = models.ImageField(upload_to='uploads/thumb/')
    pdf = models.ImageField(upload_to='uploads/pdf/')


    def __str__(self) -> str:
        return self.name
