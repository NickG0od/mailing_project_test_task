from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from mailing__client import urls as mailing__client_urls
from mailing__mailing import urls as mailing__mailing_urls
from mailing__message import urls as mailing__message_urls


schema_view = get_schema_view(
    openapi.Info(
        title="Mailing API (Testing task)",
        default_version='v1',
        description="This is API for testing task <Mailing>.",
        contact=openapi.Contact(email="shavnick.main@gmail.com"),
        license=openapi.License(name="Mailing IP"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('clients/', include(mailing__client_urls)),
    path('mailings/', include(mailing__mailing_urls)),
    path('messages/', include(mailing__message_urls)),
]

