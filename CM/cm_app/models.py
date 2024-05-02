from django.db import models

# Create your models here.
class Collection(models.Model):
    collection_name = models.CharField(max_length = 20)

class Item(models.Model):
    name = models.CharField(max_length = 20)
    fabric = models.CharField(max_length = 20)
    care_instructions = models.TextField()
    price = models.PositiveSmallIntegerField()
    collection = models.ForeignKey(
        Collection,
        related_name = 'item',
        on_delete = models.CASCADE,
    )
