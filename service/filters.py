from datetime import datetime

import django_filters
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Q

from service.models import Shop


class ShopFilter(django_filters.FilterSet):
    city = django_filters.CharFilter(field_name='city__name')
    street = django_filters.CharFilter(field_name='street__name')
    open = django_filters.NumberFilter(method='is_open_filter', validators=[MinValueValidator(0), MaxValueValidator(1)])

    class Meta:
        model = Shop
        fields = ['city', 'street', 'open']

    def is_open(self, queryset, name, value):
        now = datetime.now().time()

        if int(value) == 0:
            return queryset.filter(Q(opening__gte=now) | Q(closing__lte=now))
        else:
            return queryset.filter(opens_at__lte=now, closes_at__gte=now)