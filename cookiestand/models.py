from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class CookieStand(models.Model):
    name = models.CharField(max_length=256)
    #make sure from the names here

    reviewer = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    # make sure from the (name of) reviewer ,cuz we will send it in creat.html & update.html as .reviewer --> like this  ({% for value, choice in form.fields.reviewer.choices %}

    description = models.TextField(default="", null=True, blank=True)
    hourly_sales = models.JSONField(default=list, null=True)
    minimum_customers_per_hour = models.IntegerField(default=0)
    maximum_customers_per_hour = models.IntegerField(default=0)
    average_cookies_per_sale = models.FloatField(default=0)
    rating = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.name
    # make sure from the names here


    def get_absolute_url(self):
        return reverse('cookiestand_detail', args=[str(self.id)])

