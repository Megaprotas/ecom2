from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(default='default.jpg', upload_to='upload_pics')

    def __str__(self):
        return f'{self.user.username}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        photo = Image.open(self.photo.path)
        if photo.height > 100 or photo.width > 100:
            new_size = (100, 100)
            photo.thumbnail(new_size)
            photo.save(self.photo.path)


class AboutUs(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.title
