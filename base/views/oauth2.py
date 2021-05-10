import base64
import json
import requests
from django.shortcuts import redirect

from base.settings.base_settings import HOST, OAUTH2_PROVIDERS
from base.utils import django_login
from base.views import BasePublicAPIView


class BaseGoogleLoginCallbackView(BasePublicAPIView):
    provider_name = 'GOOGLE'
    model_class = None

    def get(self, request, *args, **kwargs):
        provider = OAUTH2_PROVIDERS.get(self.provider_name)
        if request.GET.get('code'):
            uri = provider.get('TOKEN_URI')
            data = {
                'grant_type': 'authorization_code',
                'client_id': provider['CLIENT_ID'],
                'client_secret': provider['SECRET'],
                'redirect_uri': provider['CALLBACK_URI'],
                'code': request.GET.get('code'),
                'state': request.GET.get('state')
            }
            token_response = requests.post(uri, data=data,
                                           headers={'Content-Type': 'application/x-www-form-urlencoded'}).json()
        else:
            token_response = {
                'access_token': request.GET.get('access_token'),
                'state': request.GET.get('state'),
                'expires_in': request.GET.get('expires_in'),
            }

        payload = token_response['id_token'].split('.')[1]
        payload += '=' * (4 - (len(payload) % 4))
        payload = base64.b64decode(payload).decode('utf-8')
        google_data = json.loads(payload)
        google_data['access_token'] = token_response['access_token']
        google_data['expires_in'] = token_response['expires_in']

        google_id = google_data.get('sub')
        userquery = self.model_class.objects.filter(google_id=google_id)
        if userquery.exists():
            user = userquery.first()
        else:
            user = self.model_class.objects.create(username=f'oauth2-{self.provider_name}-{google_id}',
                                                   google_id=google_id, google_data=google_data)
        django_login(request, user)
        return redirect(f'{HOST}/close')


class BaseOAuth2LoginView(BasePublicAPIView):
    provider_name = None

    def get(self, request, *args, **kwargs):
        provider = OAUTH2_PROVIDERS.get(self.provider_name)
        return redirect(provider['LOGIN_URI'].format(provider, 'none'))
