from django.utils.functional import cached_property
from rest_framework.serializers import ModelSerializer


class BaseSerializer(ModelSerializer):
    @cached_property
    def request(self):
        return self.context.get('request')

    @cached_property
    def user(self):
        user = self.request.user
        if user and user.is_authenticated:
            return self.request.user
        else:
            return None
