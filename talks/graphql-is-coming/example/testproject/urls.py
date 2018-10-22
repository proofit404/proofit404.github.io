from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/', admin.site.login),
    url(
        r'^taskmanager/',
        include('taskmanager.urls', namespace='taskmanager'),
    ),
    url(
        r'^$',
        RedirectView.as_view(pattern_name='taskmanager:graphql'),
        name='home',
    ),
]
