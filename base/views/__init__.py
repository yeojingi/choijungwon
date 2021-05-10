from datetime import timedelta

import requests
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from base.mixins import BasePublicAPIMixin, BaseAPIMixin
from base.settings.base_settings import OAUTH2_PROVIDERS
from base.utils import django_login, parse_datetime
from practice.practice.models import User


class BasePublicAPIView(BasePublicAPIMixin, GenericAPIView):
    pass


class BaseAPIView(BaseAPIMixin, GenericAPIView):
    pass


class BasePublicModelViewSet(BasePublicAPIMixin, ModelViewSet):
    pass


class BaseModelViewSet(BaseAPIMixin, ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']
    model_class = None
    queryset = User.objects.none()

    def get_queryset(self):
        return self.model_class.objects.filter(user=self.user).order_by('id')

    def get_permissions(self):
        if self.action not in SAFE_METHODS:
            return [IsAuthenticated()]
        return [AllowAny()]

    def perform_create(self, serializer):
        serializer.save(user=self.user)

    def perform_update(self, serializer):
        serializer.save(user=self.user)


class BaseUserModelViewSet(BaseModelViewSet):
    def get_queryset(self):
        return self.model_class.objects.filter(pk=self.user.pk)

    def get_permissions(self):
        if self.action in ['create', 'list']:
            return [AllowAny()]
        return super().get_permissions()

    def get_object(self):
        return self.user

    def list(self, request, *args, **kwargs):
        if self.user:
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.ok_response('LOGIN_REQUIRED', status=status.HTTP_204_NO_CONTENT)

    def perform_create(self, serializer):
        user = serializer.save()
        password = serializer.initial_data.get('password')
        user.set_password(password)
        user.save()
        django_login(self.request, user)

    def perform_update(self, serializer):
        user = serializer.save()
        password = serializer.initial_data.get('password')
        if password and user.google_id is None:
            user.set_password(password)
            user.save()
            django_login(self.request, user)

    def perform_destroy(self, instance):
        if instance.google_id is not None:
            provider_settings = OAUTH2_PROVIDERS['GOOGLE']
            requests.get(provider_settings['DROPOUT_URI'].format(instance.google_data['access_token']), headers={})
        instance.delete()


class BaseCalendarModelViewSet(BaseModelViewSet):
    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        days = data.get('days')
        datetime = parse_datetime(data.get('datetime'))
        if days:
            serializer = self.get_serializer(
                data=[{**data, 'datetime': datetime + timedelta(days=day)} for day in range(days)],
                many=days is not None)
        else:
            serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
