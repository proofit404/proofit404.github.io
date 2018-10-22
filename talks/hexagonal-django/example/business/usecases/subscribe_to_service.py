import attr

from ..entities import Customer, Service, Subscription


@attr.s
class Subscribe:

    repository = attr.ib()

    def __call__(self, customer_name, service_name, date, days):

        subscription = Subscription(
            Customer(customer_name),
            Service(service_name),
            date,
            days,
        )
        self.repository.store(subscription)
        return "You subscribe to {service} for {days} days".format(
            service=service_name,
            days=days,
        )
