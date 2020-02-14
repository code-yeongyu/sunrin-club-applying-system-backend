from django.contrib import admin
from django.urls import path, include

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Plaon APIs",
        default_version='v1',
    ),
    validators=['flex'],
    public=True,
    # permission_classes=(permissions.AllowAny, ),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # added by fastdj
    path('application/', include('application.urls'), name='application'),
    # added by fastdj
    path('custom_user/', include('custom_user.urls'), name='custom_user'),
    path('swagger/',
         schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui')
]
