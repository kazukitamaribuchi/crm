from django.db import models
from django.utils.translation import ugettext_lazy as _
from .db.base import (
    AbstractHumanModel,
    AbstractServiceModel,
)
from .db.sub_models import (
    CardManagement,
)
import os, uuid, logging

logger = logging.getLogger(__name__)





class MCustomer(AbstractHumanModel):
    """
    顧客マスタ
        総売り上げ
        総来店回数
        所属
    """
    job = models.CharField(
        _('Job'),
        null=True,
        blank=True,
        max_length=100,
    )
    company = models.CharField(
        _('Company'),
        null=True,
        blank=True,
        max_length=100,
    )
    total_visit = models.IntegerField(
        _('Total Visit'),
        default=0,
    )
    total_sales = models.BigIntegerField(
        _('Total Sales'),
        default=0,
    )
    first_visit = models.DateField(
        _('First Visit'),
        null=True,
        blank=True,
    )
    rank = models.OneToOneField(
        'api.Rank',
        on_delete=models.PROTECT,
    )
    card = models.OneToOneField(
        'api.CardManagement',
        on_delete=models.PROTECT,
    )
    caution_flg = models.BooleanField(
        _('Caution Flg'),
        default=False,
    )



class MCast(AbstractHumanModel):
    """
    キャストマスタ
    """
    icon = models.ImageField(
        _('Cast Image'),
        upload_to='upload/',
        null=True,
        blank=True,
    )
    real_name = models.CharField(
        _('Real Name'),
        max_length=100,
        null=True,
        blank=True,
    )
    real_age = models.SmallIntegerField(
        _('Real Age'),
        null=True,
        blank=True,
    )
    start_working_date = models.DateField(
        _('Start Working Date'),
        null=True,
        blank=True,
    )
    total_appoint = models.IntegerField(
        _('Total appoint'),
        default=0,
    )
    resign_flg = models.BooleanField(
        _('Delete Flg'),
        default=False,
    )
    resign_date = models.DateTimeField(
        _('Resign Date'),
        null=True,
        blank=True,
    )
    # 今後考える？・・・
    salary = models.IntegerField(
        _('Salary'),
        default=0,
        null=True,
        blank=True,
    )



class MProduct(AbstractServiceModel):
    """
    商品マスタ
        商品名
        商品カテゴリ
        金額（税区分によって
    """

    PRODUCT_CATEGORIES = (
        (0, _('飲食')),
        (1, _('指名料（同伴含む）')),
        (2, _('基本料金')),
        (3, _('席料金')),
        (4, _('他')),
    )

    category = models.SmallIntegerField(
        _('Category'),
        choices=PRODUCT_CATEGORIES,
        max_length=30,
        default=0,
    )

    tax = models.OneToOneField(
        'api.MTax',
        on_delete=models.SET_NULL,
    )

    tax_price = models.IntegerField(
        _('Price included Tax'),
    )




class MRank(AbstractBaseModel):
    """
    顧客のランクマスタ
        1:ノーマル
        2:シルバー
        3:ゴールド
        4:プラチナ
        5:ブラック
        ※将来的な拡張性も考えてテーブルで管理する
    """
    RANK_CHOICES = (
        (1, _('Normal')),
        (2, _('Silver')),
        (3, _('Gold')),
        (4, _('Platinum')),
        (5, _('Black')),
    )

    rank = models.SmallIntegerField(
        _('Rank'),
        choices=RANK_CHOICES
        default=1,
    )





class MTax(AbstractBaseModel):
    """
    税区分（必要に応じて追加
        ・0%（非課税）
        ・15%
    """
    TAX_CHOICES = (
        (0, _('非課税')),
        (8, _('8%')),
        (10, _('10%')),
        (15, _('15%')),
    )

    tax_rate = models.SmallIntegerField(
        _('Price included Tax'),
        default=15,
    )



class MSeat(TimeStampModel):
    """
    座席マスタ
        予約と紐づけ
    """

    SEAT_TYPE_CHOICES = (
        (0, _('VIP')),
        (1, _('Normal')),
    )

    seat_type = models.SmallIntegerField(
        _('Seat Type'),
        choices=SEAT_TYPE_CHOICES,
    )

    seat_no = models.SmallIntegerField(
        _('Seat No'),
    )

    limit = models.SmallIntegerField(
        _('Limit'),
        default=1,
    )
