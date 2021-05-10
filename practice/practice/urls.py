from django.urls import include, path
from rest_framework import routers

from practice.practice.views import LogoutAPIView, LoginAPIView, UserViewSet, BabyViewSet, \
    MemoViewSet, TipViewSet, CalendarViewSet, \
    GoogleLoginCallbackView, GoogleLoginView, index, close

api_router = routers.SimpleRouter()
api_router.register(r'user', UserViewSet)
api_router.register(r'baby', BabyViewSet)
api_router.register(r'memo', MemoViewSet)
api_router.register(r'tip', TipViewSet)
api_router.register(r'calendar', CalendarViewSet)

urlpatterns = [
    path('', include([
        path('', index, name='index'),
        path('close', close, name='close'),
    ])),
    path('api/', include(api_router.urls)),
    path('auth/', include([
        path('login/', LoginAPIView.as_view(), name='login'),
        path('logout/', LogoutAPIView.as_view(), name='logout'),
    ])),
    path('oauth2/', include([
        path('google/callback/', GoogleLoginCallbackView.as_view(), name='oauth2-google-callback'),
        path('google/login/', GoogleLoginView.as_view(), name='oauth2-google-login'),
    ])),
]
