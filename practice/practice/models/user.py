from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.utils.timezone import now
from base.models import models


class User(AbstractBaseUser):
    USERNAME_FIELD = 'username'
    username = models.CharField(max_length=100, unique=True)  # 아이디
    google_id = models.CharField(max_length=100, null=True)  # null이면 그냥로그인
    google_data = models.JSONField(null=True)
    objects = UserManager()


class Baby(models.Model):
    user = models.ForeignKey('User', related_name='babies', on_delete=models.CASCADE)  # 부모
    name = models.CharField(max_length=20)
    birth = models.DateField(default=now)
