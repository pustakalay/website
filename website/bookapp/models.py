from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Book(models.Model):

    def __str__(self):
        return self.title
    LANGUAGE_CHOICES = (
        ('HINDI','Hindi'),
        ('ENGLISH','English'),
        ('MARATHI', 'Marathi')
    )
    FORMAT_CHOICES = (
        ('PAPERBACK', 'Paperback'),
        ('HARDCOVER', 'Hardcover'),
        ('EBOOK', 'Ebook')
    )
    title = models.CharField(max_length=200)
    displayTitle = models.CharField(max_length=200,blank=True)
    author = models.CharField(max_length=200)
    language = models.CharField(max_length=200,choices=LANGUAGE_CHOICES,default='English')
    format = models.CharField(max_length=200,choices=FORMAT_CHOICES,default='Paperback')
    publisher = models.CharField(max_length=200)
    publishingDate = models.DateField(auto_now=True,blank=True)
    isbn10 = models.CharField(max_length=200,unique=True,blank=True)
    isbn13 = models.CharField(max_length=200, unique=True,blank=True)
    dimension = models.CharField(max_length=200)
    weight = models.FloatField()
    numberOfPages = models.BigIntegerField()
    category = models.CharField(max_length=200,blank=True)
    subCategory = models.CharField(max_length=200,blank=True)
    edition = models.CharField(max_length=200,blank=True)
    numberOfCopiesSold = models.BigIntegerField(default=0)
    pustakalayRating = models.FloatField(default=0,validators=[MaxValueValidator(5), MinValueValidator(1)])
    avgcustomerRating = models.BigIntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(1)])
    newArrival = models.FloatField(default=0, validators=[MaxValueValidator(5), MinValueValidator(1)]) ##auto decrement
    context = models.CharField(max_length=200,blank=True)
    rank = models.FloatField(default=0)
    translatedBy = models.CharField(max_length=200,blank=True)
    sku = models.CharField(default='pu',max_length=200, unique=True,blank=True)
    price = models.BigIntegerField(default=200)
    maxretailprice = models.BigIntegerField(default=200)
    minimumprice = models.BigIntegerField(default=200)
    discount = models.BigIntegerField(default=200)
    inventory = models.BigIntegerField(default=200)
    description = models.TextField(max_length=20000)
    author = models.TextField(max_length=20000,blank=True)
    image_front = models.ImageField(blank=True)
    image_back = models.ImageField(blank=True)