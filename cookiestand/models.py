from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class CookieStand(models.Model):
    # name = models.CharField(max_length=256)
    # rating = models.IntegerField(default=0, blank=True)
    # reviewer = models.ForeignKey(
    #     get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    # )
    # description = models.TextField(default="", null=True, blank=True)

    # def __str__(self):
    #     return self.name
      
    name = models.CharField(max_length=256)
    reviewer = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    description = models.TextField(default="", null=True, blank=True)
    hourly_sales = models.JSONField(default=list, null=True)
    minimum_customers_per_hour = models.IntegerField(default=0)
    maximum_customers_per_hour = models.IntegerField(default=0)
    average_cookies_per_sale = models.FloatField(default=0)
    rating = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cookiestand_detail', args=[str(self.id)])

