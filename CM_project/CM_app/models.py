from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Collection(models.Model):
    collection_name = models.CharField(max_length = 20)

class Care(models.Model):
    fabric = models.CharField(max_length = 20)
    care = models.TextField()

class Item(models.Model):
    name = models.CharField(max_length = 20)
    price = models.PositiveSmallIntegerField()
    picture = models.ImageField(upload_to='img', default='')
    fabric = models.ForeignKey(
        Care,
        related_name= 'item',
        on_delete=models.CASCADE
    )
    collection = models.ForeignKey(
        Collection,
        related_name = 'item',
        on_delete = models.CASCADE
    )
    def __str__(self):
        return self.name

class Cart(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.ForeignKey(
        User,
        on_delete= models.CASCADE
        )
    completed = models.BooleanField(default=False)
    def __str__(self):
        return str(self.id)

class CartItem(models.Model):
    commodity = models.ForeignKey(
        Item,
        related_name='cart_commodities',
        on_delete = models.CASCADE
    )
    cart = models.ForeignKey(
        Cart,
        related_name='cart_item',
        on_delete= models.CASCADE
    )
    quantity = models.PositiveSmallIntegerField(default=0)
    