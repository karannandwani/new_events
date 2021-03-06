
from django.db import models
from datetime import datetime, timedelta, timezone
from django.contrib.auth.models import User
import pytz
import django.utils.timezone
# Create your models here.

category = ()
cluster_choices = (('1', '1'), ('2', '2'))


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class events(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True)
    summary = models.TextField(max_length=500)
    picture = models.ImageField(upload_to="event_posters")
    rules = models.TextField(max_length=2000, default="")
    payment_script = models.TextField(max_length=1000, default="")
    cost = models.IntegerField(default=0)
    cost2 = models.IntegerField(default=0, blank=True)
    cost3 = models.IntegerField(default=0, blank=True)
    total_revenue = models.IntegerField(default=0)
    participants = models.IntegerField(default=0)
    start_day = models.DateField(default=django.utils.timezone.now)
    email = models.EmailField(
        default='prodigygamer143@gmail.com', max_length=50)
    password = models.CharField(default='8017586761', max_length=100)
    group_event = models.BooleanField(default=False)
    registration_data = models.FileField(upload_to='reg_data', default="")
    eventadmin = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Events"

    def __str__(self):
        return self.name


class registration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    number = models.CharField(max_length=20)
    link = models.CharField(blank=True, max_length=500)
    referral = models.CharField(blank=True, max_length=50)
    coupon = models.CharField(blank=True, max_length=50)
    event = models.CharField(max_length=100, default='Null')
    cost = models.CharField(max_length=4, default='100')
    paid = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=200, blank=True)
    participant_id = models.CharField(max_length=10, blank=True)
    timestamp = models.DateTimeField(
        blank=True, default=django.utils.timezone.now)
    day_registered = models.DateField(
        blank=True, default=django.utils.timezone.now)

    class Meta:
        verbose_name_plural = "Registrations"

    def __str__(self):
        return self.name


class date_revenue(models.Model):
    event_key = models.ForeignKey(events, on_delete=models.CASCADE)
    day = models.DateField()
    revenue = models.IntegerField()
    no_of_participants = models.IntegerField()

    def __str__(self):
        return str(self.event_key) + " " + str(self.day)[-5:]


class society_leads(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(events, on_delete=models.CASCADE)

    def __str__(self):
        return self.event.name


class state_connection(models.Model):
    state_choices = category
    state_name = models.CharField(max_length=30)
    state_connected_to = models.CharField(max_length=50, choices=state_choices)

    def __str__(self):
        return self.state_name


class coupons(models.Model):
    event = models.ForeignKey(events, on_delete=models.CASCADE)
    code = models.CharField(max_length=50)
    discount_amount = models.CharField(max_length=4)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.code
