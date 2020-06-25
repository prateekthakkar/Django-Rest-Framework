from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    author = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title