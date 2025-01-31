from django.db.models import Prefetch
from rest_framework.viewsets import ReadOnlyModelViewSet

from .serializers import FoodListSerializer
from food.models import Food, FoodCategory


class FoodsViewSet(ReadOnlyModelViewSet):
    queryset = FoodCategory.objects.prefetch_related(
        Prefetch("food", queryset=Food.objects.filter(is_publish=True))
    ).filter(food__is_publish=True).distinct()
    serializer_class = FoodListSerializer
