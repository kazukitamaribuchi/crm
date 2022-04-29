from django.db import models
from django.utils.translation import ugettext_lazy as _
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
    RANK_CHOICES = (
        (1, _('Normal')),
        (2, _('Silver')),
        (3, _('Gold')),
        (4, _('Platinum')),
        (5, _('Black')),
    )

    rank = models.SmallIntegerField(
        _('Rank'),
        choices=RANK_CHOICES,
        default=1,
    )

    def __str__(self):
        return str(self.rank)

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
    )

    tax_rate = models.SmallIntegerField(
        _('Price included Tax'),
        choices=TAX_CHOICES,
        default=15,
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
    rank = models.ForeignKey(
        MRank,
        on_delete=models.PROTECT,
    )
    card = models.OneToOneField(
        'crm.CardManagement',
        on_delete=models.PROTECT,
    )
    caution_flg = models.BooleanField(
        _('Caution Flg'),
        default=False,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '顧客マスタ'


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

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'キャストマスタ'


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
        default=0,
    )

    tax = models.ForeignKey(
        MTax,
        on_delete=models.PROTECT,
    )

    tax_price = models.IntegerField(
        _('Price included Tax'),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '商品マスタ'



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

    def show_str(self, type, no):
        return str(self.SEAT_TYPE_CHOICES[type][1] + str(no))

    def __str__(self):
        return self.show_str(self.seat_type, self.seat_no)

    class Meta:
        verbose_name_plural = '席マスタ'
