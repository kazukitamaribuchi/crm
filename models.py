from django.db import models
from django.utils.translation import ugettext_lazy as _
from .core import (
    TimeStampModel
)
import os, uuid, logging

logger = logging.getLogger(__name__)


class TimeStampModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class MCustomer(TimeStampModel):
    """
    顧客マスタ
        総売り上げ
        総来店回数
        所属
    """
    customer_id = models.UUIDField(
        _('Customer Id'),
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    real_name = models.CharField(
        _('Real Name'),
        max_length=50,
    )
    name = models.CharField(
        _('Name included Nickname')
        max_length=50
    )
    age = models.SmallIntegerField(
        _('Age'),
        null=True,
        blank=True
    )
    address = models.CharField(
        _('Address'),
        null=True,
        blank=True,
    )
    first_visit = models.DateTimeField(
        _('First Visit'),
    )
    rank = models.OneToOneField(
        Rank,
        on_delete=models.DO_NOTHING,
    )
    birthday = models.DateField(
        _('Birth Day'),
        null=True,
        blank=True,
    )


class MRank(TimeStampModel):
    """
    顧客のランクマスタ
        5:ブラック
        4:プラチナ
        3:ゴールド
        2:シルバー
        1:ノーマル
        ※将来的な拡張性も考えてテーブルで管理する
    """
    RANK_DIST = {
        1: 'Normal',
        2: 'Silver',
        3: 'Gold',
        4: 'Platinum',
        5: 'Black'
    }

    level = models.IntegerField(
        _('Rank'),
        default=1
    )

    level_name = models.CharField(
        max_length=20,
        default=RANK_DIST[level]
    )

    description = models.TextField(
        _('Description'),
        null=True,
        black=True
    )


class MCast(TimeStampModel):
    """
    キャストマスタ
    """
    real_name = models.CharField(
        _('Real Name'),
        max_length=50,
        null=True,
        blank=True,
    )
    name = models.CharField(
        _('Name included Nickname')
        max_length=50
    )
    real_age = models.SmallIntegerField(
        _('Real Age'),
        null=True,
        blank=True,
    )
    age = models.SmallIntegerField(
        _('Age'),
        null=True,
        blank=True,
    )
    address = models.CharField(
        _('Address'),
        null=True,
        blank=True,
    )
    birthday = models.DateField(
        _('Birth Day'),
        null=True,
        blank=True,
    )

class MProduct(models.Model):
    """
    商品マスタ
        商品名
        商品カテゴリ
        金額（税区分によって
    """

    price = models.

class ProductCategory(models.Model):
    """
    商品のカテゴリ

    """

class mBottle(TimeStampModel):
    """
    ボトルマスタ
        商品名
        開栓日
    """

class Tax(models.Model):
    """
    税区分
    """


class SalesHeader(TimeStampModel):
    """
    会計ヘッダ
        会計日
        総額
        顧客(1)
        担当(n)
    """


class SalesDetail(TimeStampModel):
    """
    会計明細
    """
    header = models.ForeignKey(
        SalesHeader,
        on_delete=models.CASCADE,
        related_name='sales_header'
    )


class Booling(TimeStampModel):
    """
    予約情報
        開始時間
        終了時間
        席
        担当
        顧客
        キャンセルフラグ
        終了フラグ
        人数
    """

class MSeat(models.Model):
    """
    座席マスタ
        予約と紐づけ
    """
