from datetime import datetime

import attr
from attr.validators import instance_of

from .customer import Customer
from .service import Service


@attr.s
class Subscription:

    customer = attr.ib(validator=instance_of(Customer))
    service = attr.ib(validator=instance_of(Service))
    subscribe_date = attr.ib(validator=instance_of(datetime))
    days = attr.ib(validator=instance_of(int))
