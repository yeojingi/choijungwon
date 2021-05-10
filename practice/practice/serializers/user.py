from base.serializer import BaseSerializer
from base.utils import extra_kwargs
from practice.practice.models import User, Baby


class UserSerializer(BaseSerializer):
    class Meta:
        model = User
        exclude = ('google_id', 'google_data', 'last_login',)
        extra_kwargs = extra_kwargs('password', )


class BabySerializer(BaseSerializer):
    class Meta:
        model = Baby
        fields = '__all__'
        extra_kwargs = extra_kwargs('user', )
