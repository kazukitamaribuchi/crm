from django.db import models
from django.utils.translation import ugettext_lazy as _
from .core.models import (
    TimeStampModel
)

from .sub_models import (
)


class AbstractBaseModel(TimeStampModel):
    """
    全てのベースとなる基本モデル
    """
    delete_flg = models.BooleanField(
        _('Delete Flg'),
        default=False,
    )
    remarks = models.TextField(
        _('Remarks Columns'),
        null=True,
        blank=True,
    )
    class Meta:
        abstract = True

class AbstractHumanModel(AbstractBaseModel):
    """
    顧客、キャストの基となる抽象クラス
    """
    name = models.CharField(
        _('NickName'),
        max_length=100,
    )
    age = models.SmallIntegerField(
        _('Age for Profile'),
        null=True,
        blank=True,
    )
    address = models.CharField(
        _('Address'),
        null=True,
        blank=True,
        max_length=200,
    )
    birthday = models.DateField(
        _('Birthday'),
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True


class AbstractServiceModel(AbstractBaseModel):
    """
    サービスの基となる抽象クラス
    """
    name = models.CharField(
        _('Service Name'),
        max_length=200,
    )

    price = models.IntegerField(
        _('Price'),
    )
