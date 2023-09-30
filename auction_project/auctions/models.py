from django.db import models
from accounts.models import CustomUser


class Auction(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    start_price = models.DecimalField(max_digits=10, decimal_places=2)
    item_name = models.CharField(max_length=100)
    winner = models.ForeignKey(
        CustomUser, null=True, blank=True, on_delete=models.SET_NULL)
