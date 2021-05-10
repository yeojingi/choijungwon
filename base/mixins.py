from django.utils.functional import cached_property
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from base.authentication import CsrfExemptSessionAuthentication
from base.utils import _t


class BasePublicAPIMixin:
    @cached_property
    def user(self):
        user = self.request.user
        if user and user.is_authenticated:
            return self.request.user
        else:
            return None

    authentication_classes = [CsrfExemptSessionAuthentication, ]

    @staticmethod
    def ok_response(code='', results=None, status=200):
        if results is None:
            results = []
        return Response({
            'success': True,
            'results': results,
            'code': code,
            'message': _t(code)
        }, status=status, headers={
            'Access-Control-Allow-Headers': '*',
            'access-control-allow-origin': '*'
        })

    @staticmethod
    def err_response(code, status=400):
        return Response({
            'success': False,
            'code': code,
            'message': _t(code)
        }, status=status, headers={
            'Access-Control-Allow-Headers': '*',
            'access-control-allow-origin': '*'
        })


class BaseAPIMixin(BasePublicAPIMixin):
    permission_classes = [IsAuthenticated]
