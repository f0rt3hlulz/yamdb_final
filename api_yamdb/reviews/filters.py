import django_filters as filters

from .models import Title


class TitleFilter(filters.FilterSet):
    genre = filters.CharFilter(field_name='genre__slug', lookup_expr='iexact')
    category = filters.CharFilter(
        field_name='category__slug',
        lookup_expr='iexact'
    )
    year = filters.NumberFilter(field_name='year', lookup_expr='iexact')
    name = filters.CharFilter(field_name='name', lookup_expr='contains')

    class Meta:
        model = Title
        fields = (
            'id', 'name', 'year', 'genre', 'category'
        )
