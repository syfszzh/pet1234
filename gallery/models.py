from django.db import models

class GalleryImage(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='gallery_images/')

    def __str__(self):
        return self.title