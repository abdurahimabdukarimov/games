from django.db import models

# Create your models here.
class Products(models.Model):
    name=models.CharField(max_length=300)
    bio=models.TextField()
    img=models.ImageField(upload_to='product/img')
    price=models.IntegerField()

    def __str__(self):
        return self.name

class Comment(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()
    img = models.ImageField(upload_to='comment/img')

    def __str__(self):
        return self.name

class Video(models.Model):
    name=models.CharField(max_length=300)
    bio=models.TextField()
    img=models.ImageField(upload_to='video/img')
    price=models.IntegerField()

    def __str__(self):
        return self.name
class Remot(models.Model):
    name=models.CharField(max_length=300)
    bio=models.TextField()
    img=models.ImageField(upload_to='remot/img')
    price=models.IntegerField()

    def __str__(self):
        return self.name


