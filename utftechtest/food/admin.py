from django.contrib.admin import ModelAdmin, register, site
from django.contrib.auth.models import Group, User

from .models import Food, FoodCategory


site.unregister(Group)
site.unregister(User)


@register(Food)
class FoodAdmin(ModelAdmin):
    """Food in admin panel."""
    list_display = (
        'name_ru', 'category', 'description_ru', 'cost', 'is_publish'
    )


@register(FoodCategory)
class FoodCategoryAdmin(ModelAdmin):
    """Food categories in admin panel."""
    list_display = ('name_ru',)
