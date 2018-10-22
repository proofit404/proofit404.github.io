from django.conf.urls import url

from .views import ApplySubscription, ServiceList

urlpatterns = [
    url(r'^list/$', ServiceList.as_view(), name='list-services'),
    url(r'^subscribe/$',
        ApplySubscription.as_view(),
        name='subscribe-to-service'),
]
