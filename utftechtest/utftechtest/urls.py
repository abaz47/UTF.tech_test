"""
URL configuration for utftechtest project.
"""
from django.contrib import admin
from django.urls import include, path

from api.urls import v1_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(v1_router.urls)),
]
