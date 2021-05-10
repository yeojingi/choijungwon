from django.contrib import auth as django_auth
from rest_framework import status
from rest_framework.response import Response

from base.utils import django_login
from base.views import BasePublicAPIView, BaseAPIView


class BaseLoginAPIView(BasePublicAPIView):
    model_class = None
    serializer_class = None

    def post(self, request, *args, **kwargs):
        if not self.model_class.objects.filter(username=request.data.get('username')).exists():
            return self.err_response('AUTH_WRONG_USERNAME', status=status.HTTP_401_UNAUTHORIZED)
        user = django_auth.authenticate(request, **request.data)
        if user is not None and user.is_active:
            django_login(self.request, user, auto_login=request.data.get('auto_login'))
            return Response(self.serializer_class(user).data)
        else:
            return self.err_response('AUTH_WRONG_PASSWORD', status=status.HTTP_401_UNAUTHORIZED)


class BaseLogoutAPIView(BaseAPIView):
    def get(self, request, *args, **kwargs):
        django_auth.logout(request)
        return self.ok_response('LOGOUT_SUCCEEDED')
