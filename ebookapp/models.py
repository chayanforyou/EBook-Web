from django.db import models
from django.core.validators import FileExtensionValidator

class Book(models.Model):
    name = models.CharField(max_length=255)
    thumb = models.ImageField(upload_to='uploads/thumb/', validators=[FileExtensionValidator(allowed_extensions=["jpeg", "jpg", "png"])])
    pdf = models.FileField(upload_to='uploads/pdf/', validators=[FileExtensionValidator(allowed_extensions=["pdf"])])

    def __str__(self) -> str:
        return self.name
