from django.db import models

# Create your models here.

class MyModel(models.Model):
    color = models.CharField(max_length=255)
    speed = models.PositiveIntegerField()
    model = models.CharField(max_length=255)
    tags = models.CharField(max_length=255, default='')

class Account(models.Model):
    account_username = models.CharField(max_length=255, unique=True)
    account_description = models.TextField()
    account_followers = models.IntegerField()
    account_following = models.IntegerField()
    account_posts = models.IntegerField()

class Category(models.Model):
    category_name = models.CharField(max_length=255)
    def __str__(self):
        return self.category_name


class Origin(models.Model):
    lang = models.CharField(max_length=255)
    def __str__(self):
        return self.lang

class Book(models.Model):
    book_name = models.CharField(max_length=255)
    book_price = models.IntegerField()
    book_origin = models.ForeignKey(Origin,on_delete=models.CASCADE)
    book_category = models.ManyToManyField(Category, related_name="books")

    def __str__(self):
        return self.book_name

