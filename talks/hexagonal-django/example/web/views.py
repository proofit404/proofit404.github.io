from business.usecases.subscribe_to_service import Subscribe
from db.models import Service
from db.repositories import SubscriptionRepository
from dependencies import Injector
from django.http import HttpResponse
from django.utils import timezone
from django.views import View
from django.views.generic import ListView


# NOTE: I'm too lazy for fully qualified example.  This should be
# implemented through business layer too.
class ServiceList(ListView):

    model = Service
    context_object_name = 'services'
    template_name = 'web/service_list.html'


class ApplySubscription(View):

    def post(self, request, *args, **kwargs):

        customer_name = request.user.username
        servise_name = request.POST['service-name']
        starts_at = timezone.now()
        days = int(request.POST['days'])
        reply = Container.action(customer_name, servise_name, starts_at, days)
        return HttpResponse(reply)


class Container(Injector):

    action = Subscribe
    repository = SubscriptionRepository
