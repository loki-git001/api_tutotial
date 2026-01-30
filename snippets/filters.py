import django_filters
from .models import Snippet

class LanguageFilter(django_filters.FilterSet):
    language = django_filters.CharFilter(field_name='language', lookup_expr='iexact')
    style = django_filters.CharFilter(field_name='style', lookup_expr='icontains')

    class Meta:
        model = Snippet
        fields = ['language', 'style']

    