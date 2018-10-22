from django.conf.urls import include, url
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^$', RedirectView.as_view(url=reverse_lazy('list-services'))),
    url(r'^shop/', include('web.urls')),
    url(r'^admin/', admin.site.urls),
]
