from django.contrib.auth.models import User

from .models import Service, Subscription


class SubscriptionRepository:

    def store(self, subscription):

        service = Service.objects.get(name=subscription.service.name)
        user = User.objects.get(username=subscription.customer.name)
        Subscription(
            customer=user,
            service=service,
            subscribe_date=subscription.subscribe_date,
            days=subscription.days,
        ).save()
