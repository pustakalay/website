from django.db import models

# Create your models here.

class Book(models.Model):

    def __str__(self):
        return self.title

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    translatedBy = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    publisher = models.CharField(max_length=200)
    isbn = models.CharField(max_length=200)
    dimension = models.CharField(max_length=200)
    numberOfPages = models.CharField(max_length=200)
    format = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    imageLocation = models.CharField(max_length=200)
    numberOfCopiesSold = models.BigIntegerField(default=0)