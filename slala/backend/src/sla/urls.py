
from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('graphql/', GraphQLView.as_view(graphiql=True)),
    path('admin/', admin.site.urls),
    path('api/', include('Songs.api.urls'))
]
