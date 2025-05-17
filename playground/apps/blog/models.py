from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)


class Order(models.Model):
    reference = models.CharField(max_length=20, primary_key=True)


class OrderLineItem(models.Model):
    pk = models.CompositePrimaryKey("product_id", "order_id")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
