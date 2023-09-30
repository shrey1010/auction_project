from django.contrib import admin
from . models import Auction
# Register your models here.


class AuctionAdmin(admin.ModelAdmin):
    list_display = ('id','winner', 'itme_name', 'start_time', 'end_time', 'start_price')