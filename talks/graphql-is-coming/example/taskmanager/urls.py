from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from graphene_django.views import GraphQLView

from .schema import schema

urlpatterns = [
    url(
        r'^$',
        login_required(GraphQLView.as_view(schema=schema, graphiql=True)),
        name='graphql',
    ),
]
