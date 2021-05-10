from base.views import BaseModelViewSet, BaseCalendarModelViewSet
from practice.practice.filters import MemoFilterSet, TipFilterSet, CalendarFilterSet
from practice.practice.models import Tip, Memo, Calendar
from practice.practice.serializers import MemoSerializer, TipSerializer, CalendarSerializer


class MemoViewSet(BaseModelViewSet):
    model_class = Memo
    filterset_class = MemoFilterSet
    serializer_class = MemoSerializer


class TipViewSet(BaseModelViewSet):
    model_class = Tip
    filterset_class = TipFilterSet
    serializer_class = TipSerializer


class CalendarViewSet(BaseCalendarModelViewSet):
    model_class = Calendar
    filterset_class = CalendarFilterSet
    serializer_class = CalendarSerializer
