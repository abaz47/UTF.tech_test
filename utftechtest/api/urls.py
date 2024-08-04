from rest_framework.routers import DefaultRouter

from .views import FoodsViewSet

v1_router = DefaultRouter()
v1_router.register('foods', FoodsViewSet, basename='foods')
