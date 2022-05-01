from django.db import models
from django.utils.translation import ugettext_lazy as _

class TimeStampModel(models.Model):

    created_at = models.DateTimeField(
        _('作成時間'),
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        _('更新時間'),
        auto_now=True
    )

    class Meta:
        abstract = True
