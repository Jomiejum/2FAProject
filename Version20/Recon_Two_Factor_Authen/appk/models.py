import os
import uuid
from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')


def get_image_filename(instance, filename):
    """Generate a unique filename for the image file"""
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4().hex}.{ext}"
    return os.path.join('images', filename)


class UploadedImage(models.Model):
    """Model for storing uploaded images"""
    image = models.ImageField(upload_to=get_image_filename)

    def __str__(self):
        return self.image.name
