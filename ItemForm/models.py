from django.db import models
from datetime import datetime


# Create your models here.
class Item(models.Model):
    description = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    item_type = models.CharField(max_length=15)
    sold_price = models.DecimalField(max_digits=6, decimal_places=2)
    inserted_time = models.DateTimeField(default=datetime.now, blank=True)

    def item_profit(self):
        return self.sold_price - self.cost

    def __str__(self):
        return self.description


# have one table and radio should translate into a data field
