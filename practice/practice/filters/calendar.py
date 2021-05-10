from django_filters import rest_framework as filters, NumberFilter
from practice.practice.models import Memo, Tip, Calendar


class MemoFilterSet(filters.FilterSet):
    content = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Memo
        fields = '__all__'


class TipFilterSet(filters.FilterSet):
    content = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Tip
        fields = '__all__'


class CalendarFilterSet(filters.FilterSet):
    year = NumberFilter(field_name='datetime', lookup_expr='year')
    month = NumberFilter(field_name='datetime', lookup_expr='month')
    date = NumberFilter(field_name='datetime', lookup_expr='date')
    ingredient = filters.CharFilter(field_name='recipe', lookup_expr='ingredient')

    class Meta:
        model = Calendar
        exclude=('recipe',)
