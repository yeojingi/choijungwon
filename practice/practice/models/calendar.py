from django.utils.timezone import now
from base.models import base_array, models


class Memo(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
    content = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)


class Tip(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
    content = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)


class Calendar(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
    baby = models.ForeignKey('Baby', on_delete=models.CASCADE)
    recipe = models.JSONField(default=base_array)
    datetime = models.DateTimeField(default=now)  # 먹인시각
    reaction = models.CharField(max_length=100, null=True)
