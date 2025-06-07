from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Property(models.Model):
    name = models.CharField(max_length=64, unique=True)


class Item(models.Model):
    name = models.CharField(max_length=64, unique=True)
    properties = models.ManyToManyField(Property, through="ItemProperty")


class ItemProperty(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)