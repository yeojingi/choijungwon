from base.views.auth import BaseLoginAPIView, BaseLogoutAPIView
from practice.practice.models import User
from practice.practice.serializers import UserSerializer


class LoginAPIView(BaseLoginAPIView):
    model_class = User
    serializer_class = UserSerializer


class LogoutAPIView(BaseLogoutAPIView):
    pass
