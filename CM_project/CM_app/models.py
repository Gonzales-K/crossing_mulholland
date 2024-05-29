from django.db import models

# Create your models here.
class Collection(models.Model):
    collection_name = models.CharField(max_length = 20)

class Care(models.Model):
    fabric = models.CharField(max_length = 20)
    care = models.TextField()

class Item(models.Model):
    name = models.CharField(max_length = 20)
    price = models.PositiveSmallIntegerField()
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