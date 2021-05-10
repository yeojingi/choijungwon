from django.utils.timezone import now

from base.serializer import BaseSerializer
from practice.practice.models import Calendar
from practice.practice.models.calendar import Tip, Memo
from base.utils import extra_kwargs


class MemoSerializer(BaseSerializer):
    class Meta:
        model = Memo
        fields = '__all__'
        extra_kwargs = extra_kwargs('user', )


class TipSerializer(BaseSerializer):
    class Meta:
        model = Tip
        fields = '__all__'
        extra_kwargs = extra_kwargs('user', )


class CalendarSerializer(BaseSerializer):
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['birth_from_now'] = (now().date() - instance.baby.birth).days
        return ret

    class Meta:
        model = Calendar
        fields = '__all__'
        extra_kwargs = extra_kwargs('user', 'baby', )
