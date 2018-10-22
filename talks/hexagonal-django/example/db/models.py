from django.db import models
from django.utils import timezone


class Service(models.Model):

    name = models.CharField(max_length=100)

    class Meta:

        verbose_name = 'service'
        verbose_name_plural = 'services'


class Subscription(models.Model):

    customer = models.ForeignKey('auth.User', related_name='subscriptions')
    service = models.ForeignKey('db.Service', related_name='subscriptions')
    subscribe_date = models.DateTimeField(default=timezone.now)
    days = models.IntegerField()

    class Meta:

        verbose_name = 'subscription'
        verbose_name_plural = 'subscriptions'
