from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from .db.base import (
    AbstractBaseModel,
    AbstractHumanModel,
    AbstractServiceModel,
)
from .sub_models import (
    CardManagement,
)
import os
import uuid
import logging

logger = logging.getLogger(__name__)


class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):

        if not username:
            raise ValueError('Username is required field')

        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):

        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        return self._create_user(username, email, password, **extra_fields)

class mUser(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(_('Username'), max_length=70, unique=True, blank=True, null=True)
    email = models.EmailField(_('Email'), max_length=70, unique=True)

    description = models.TextField(_('Description'))

    objects = UserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    is_staff = models.BooleanField(
        _('Staff Status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'
        ),
    )

    is_active = models.BooleanField(
        _('Active Flag'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    class Meta:
        verbose_name_plural = 'ユーザーマスタ'

    def __str__(self):
        return self.username

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)




class MRank(models.Model):
    """
    顧客のランクマスタ
        1:ノーマル
        2:シルバー
        3:ゴールド
        4:プラチナ
        5:ブラック
        ※将来的な拡張性も考えてテーブルで管理する
    """

    rank_id = models.SmallIntegerField(
        _('ランクid'),
    )

    rank_name = models.CharField(
        _('ランク名称'),
        max_length=20,
    )

    def __str__(self):
        return self.rank_name

    class Meta:
        verbose_name_plural = 'ランクマスタ'


class MTax(models.Model):
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
        (20, _('20%')),
        (30, _('30%')),
    )

    tax_rate = models.SmallIntegerField(
        _('Price included Tax'),
        choices=TAX_CHOICES,
        default=30,
    )

    def __str__(self):
        return str(self.tax_rate) + '%'

    class Meta:
        verbose_name_plural = '税マスタ'


class MCustomer(AbstractHumanModel):
    """
    顧客マスタ
        総売り上げ
        総来店回数
        所属
    """
    job = models.CharField(
        _('職業'),
        null=True,
        blank=True,
        max_length=100,
    )
    company = models.CharField(
        _('会社'),
        null=True,
        blank=True,
        max_length=100,
    )
    total_visit = models.IntegerField(
        _('総来店回数'),
        default=0,
    )
    total_sales = models.BigIntegerField(
        _('総売上'),
        default=0,
    )
    first_visit = models.DateField(
        _('初来店日'),
        null=True,
        blank=True,
    )
    rank = models.ForeignKey(
        MRank,
        on_delete=models.PROTECT,
        related_name='customer',
    )
    card = models.OneToOneField(
        'crm.CardManagement',
        on_delete=models.PROTECT,
        related_name='customer',
    )
    caution_flg = models.BooleanField(
        _('要注意人物フラグ'),
        default=False,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '顧客マスタ'
        indexes = [
            models.Index(fields=['name'], name='mcustomer_name_idx'),
            models.Index(fields=['total_sales'], name='mcustomer_total_sales_idx'),
            models.Index(fields=['rank'], name='mcustomer_rank_idx'),
        ]


class MCast(AbstractHumanModel):
    """
    キャストマスタ
    """
    icon = models.ImageField(
        _('顔写真'),
        upload_to='upload/',
        null=True,
        blank=True,
    )
    real_name = models.CharField(
        _('本名'),
        max_length=100,
        null=True,
        blank=True,
    )
    real_name_kana = models.CharField(
        _('本名(フリガナ)'),
        max_length=150,
        null=True,
        blank=True,
    )
    real_age = models.SmallIntegerField(
        _('実年齢'),
        null=True,
        blank=True,
    )
    start_working_date = models.DateField(
        _('勤務開始日'),
        null=True,
        blank=True,
    )
    total_appoint = models.IntegerField(
        _('総指名数'),
        default=0,
    )
    resign_flg = models.BooleanField(
        _('退職フラグ'),
        default=False,
    )
    resign_date = models.DateTimeField(
        _('退職日時'),
        null=True,
        blank=True,
    )
    # 今後考える？・・・
    salary = models.IntegerField(
        _('時給'),
        null=True,
        blank=True,
        default=0,
    )

    # qa = models.ManyToManyField(
    #     'crm.QuestionAnswer',
    #     blank=True,
    # )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'キャストマスタ'
        indexes = [
            models.Index(fields=['name'], name='mcast_name_idx')
        ]


class MSetting(AbstractBaseModel):
    """
    設定情報マスタ
        ・アラート系の制御
        ・予約時間のペナルティ
        ・予約上限（グループ換算☞1席何人か。何人で2席にするかなど）
    """


class MProductCategory(AbstractBaseModel):
    """
    商品のカテゴリ
    　大カテゴリ
        0: 基本料金 #削除
        1: 飲料
        2: フード
    　中カテゴリ
        【0】 #削除
            「0」:基本料金・・・pk:1
            「1」:指名料・・・pk:2
            「2」:場内指名料・・・pk:3
            「3」:VIP料金・・・pk:4
            「4」:同伴料金・・・pk:5
        【1】
            「0」:アルコール・・・
            「1」:ノンアルコール・・・pk:13
            「2」:ソフトドリンク・・・pk:14
        【2】
            「0」:メイン・・・pk:15
            「1」:サラダ・・・pk:16
            「2」:おかず・・・pk:17
            「3」:おつまみ・・・pk:18
            「4」:デザート・・・pk:19
            「5」:

    　小カテゴリ
        →飲料[0]アルコール[0]のみ。

        【1】【0】
            「0」:シャンパン・・・pk:6
            「1」:ワイン・・・pk:7
            「2」:焼酎・・・pk:8
            「3」:サワー・・・pk:9
            「4」:カクテル・・・pk:10
            「5」:日本酒・・・pk:11
            「6」:ビール・・・pk:12
            「7」:

    """

    large_category = models.SmallIntegerField(
        _('大カテゴリー'),
    )

    middle_category = models.SmallIntegerField(
        _('中カテゴリー'),
    )

    small_category = models.SmallIntegerField(
        _('小カテゴリー'),
        default=0,
    )

    def __str__(self):
        return str(self.large_category) + '-' + str(self.middle_category) + '-' + str(self.small_category)

    class Meta:
        verbose_name_plural = '商品カテゴリ'



class MPayment(AbstractBaseModel):
    """
    支払い方法マスタ
        現金:0
        カード:1
    """
    type = models.IntegerField(_('支払いタイプ'), default=0)

    tax = models.ForeignKey(
        MTax,
        on_delete=models.PROTECT,
        related_name='payment',
    )





class MService(AbstractServiceModel):
    """
    サービス情報のマスタ
        基本料金
        指名料金
        同伴料金
        延長料金
            type:
                0(基本)
                    0:A 時間分け
                    1:B 時間分け
                    2:C 時間分け
                1(指名)
                    0:指名
                    1:本指名
                    2:場内指名
                2(同伴)
                    0:同伴
                3(延長)
                    0:A 時間分け
                    1:B 時間分け

        start_tile, end_time = 21:00のようにコロン区切り4桁文字列

    """
    large_category = models.IntegerField(_('大カテゴリ'), default=0)
    middle_category = models.IntegerField(_('中カテゴリ'), default=0)

    start_time = models.CharField(_('開始時間'), max_length=10, null=True, blank=True)

    end_time = models.CharField(_('開始時間'), max_length=10, null=True, blank=True)


    description = models.TextField(
        _('説明')
    )

    tax = models.ForeignKey(
        MTax,
        on_delete=models.PROTECT,
        related_name='basic_service',
    )

    tax_price = models.IntegerField(
        _('税込価格'),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '基本料金マスタ'

class MAppointService(AbstractServiceModel):
    """
    指名料金マスタ
    """

    # 一応・・・
    thumbnail = models.ImageField(
        _('サムネイル'),
        upload_to='upload/',
        null=True,
        blank=True,
    )

    tax = models.ForeignKey(
        MTax,
        on_delete=models.PROTECT,
        related_name='appoint_service',
    )

    tax_price = models.IntegerField(
        _('税込価格'),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '指名料金マスタ'


class MProduct(AbstractServiceModel):
    """
    商品マスタ
        商品名
        商品カテゴリ
        金額（税区分によって
    """

    thumbnail = models.ImageField(
        _('サムネイル'),
        upload_to='upload/',
        null=True,
        blank=True,
    )

    category = models.ForeignKey(
        MProductCategory,
        on_delete=models.PROTECT,
        related_name='product'
    )

    tax = models.ForeignKey(
        MTax,
        on_delete=models.PROTECT,
        related_name='product',
    )

    tax_price = models.IntegerField(
        _('税込価格'),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '商品マスタ'


class MQuestion(AbstractBaseModel):
    """
    Questionマスタ
    """
    question = models.CharField(
        _('質問内容'),
        max_length=200,
    )

    def __str__(self):
        return str(self.question)

    class Meta:
        verbose_name_plural = '質問マスタ'


class MSeat(models.Model):
    """
    座席マスタ
        予約と紐づけ
    """

    SEAT_TYPE_CHOICES = (
        (0, _('VIP')),
        (1, _('Normal')),
    )

    seat_type = models.SmallIntegerField(
        _('座席種別'),
        choices=SEAT_TYPE_CHOICES,
    )

    seat_no = models.SmallIntegerField(
        _('席No'),
    )

    limit = models.SmallIntegerField(
        _('上限人数'),
        default=1,
    )

    def show_str(self, type, no):
        return str(self.SEAT_TYPE_CHOICES[type][1] + str(no))

    def __str__(self):
        return self.show_str(self.seat_type, self.seat_no)

    class Meta:
        verbose_name_plural = '席マスタ'
