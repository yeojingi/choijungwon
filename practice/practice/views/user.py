from base.views import BaseModelViewSet, BaseUserModelViewSet
from practice.practice.models import User, Baby
from practice.practice.serializers import UserSerializer, BabySerializer


class UserViewSet(BaseUserModelViewSet):
    model_class = User
    serializer_class = UserSerializer


class BabyViewSet(BaseModelViewSet):
    model_class = Baby
    serializer_class = BabySerializer
