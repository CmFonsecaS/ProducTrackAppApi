from django.db import models

class User(models.Model):
    uid = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    image = models.URLField()

    def __str__(self):
        return self.email