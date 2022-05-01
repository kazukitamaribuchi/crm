from django.db import models
from django.utils.translation import ugettext_lazy as _
from .core import (
    TimeStampModel
)


class AbstractBaseModel(TimeStampModel):
    """
    全てのベースとなる基本モデル
    """
    delete_flg = models.BooleanField(
        _('削除フラグ'),
        default=False,
    )
    remarks = models.TextField(
        _('備考'),
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
        _('名前'),
        max_length=100,
    )
    age = models.SmallIntegerField(
        _('年齢'),
        null=True,
        blank=True,
    )
    address = models.CharField(
        _('住所'),
        null=True,
        blank=True,
        max_length=200,
    )
    birthday = models.DateField(
        _('誕生日'),
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
        _('サービス名'),
        max_length=200,
    )

    price = models.IntegerField(
        _('価格'),
    )

    class Meta:
        abstract = True
