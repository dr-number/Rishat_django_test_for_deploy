from itertools import count
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=19, decimal_places=2)
    count_in_basked = models.IntegerField(default=0)

    def get_price(self):
        return str(self.price)
    
