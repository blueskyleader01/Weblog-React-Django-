from django.db import models
from django.core.files.images import get_image_dimensions
from backend.accounts.models import User # not created yet
from django.conf import settings


def validate_cover(value):
    size = get_image_dimensions(value)
    if size > settings.MAX_UPLOAD_ADMIN_SIZE:
        raise ValueError("Please keep file size under 2 MB")


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    """
        NOTE: 
            1- The user models is not created, 
            2- The author field must be null because of on_delete
            3- The descritpion will change to ckediter fields
    """
    STATUS_CHOICES = (
        ('d', 'draft'),
        ('p', "publish"),
    )
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    cover = models.ImageField(upload_to='backend/media')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.author} created {self.title}'


class AboutUsModel(models.Model):
    text = models.TextField()


class ContactUsModel(models.Model):
    title = models.CharField(max_length=100)
    phone = models.IntegerField()
    body = models.TextField()


