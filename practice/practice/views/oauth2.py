from base.views.oauth2 import BaseOAuth2LoginView, BaseGoogleLoginCallbackView
from practice.practice.models import User


class GoogleLoginView(BaseOAuth2LoginView):
    provider_name = 'GOOGLE'


class GoogleLoginCallbackView(BaseGoogleLoginCallbackView):
    model_class = User
