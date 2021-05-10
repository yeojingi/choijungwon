from datetime import timedelta

from django.contrib.sessions.models import Session
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _t
from rest_framework.fields import DateTimeField

from base.settings.settings import MEDIA_ROOT
from django.contrib import auth as django_auth


def millisec_string(max_length=None):
    import time
    millisec = str(int(round(time.time() * 1000)))
    if max_length:
        return millisec[:max_length]
    else:
        return millisec


def upload_function(instance, filename):
    return f'{instance.__class__.__name__}/{instance.id}/{filename}'


def delete_file(class_name, instance):
    import os
    import shutil
    path = os.path.join(MEDIA_ROOT, class_name, instance.id)
    if os.path.isdir(path):
        shutil.rmtree(path)


def extra_kwargs(*args):
    set_write_only = {'write_only': True}
    ret = {arg: set_write_only for arg in args}
    ret['id'] = {'read_only': True}
    return ret


def django_login(request, user, auto_login=False):
    django_auth.login(request, user)
    if auto_login:
        session, _ = Session.objects.get_or_create(session_key=request.session.session_key)
        session.expire_date = now() + timedelta(days=30)
        session.save()


def parse_datetime(date_str):
    return DateTimeField().to_internal_value(date_str)
