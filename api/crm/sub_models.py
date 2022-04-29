from django.db import models
from django.utils.translation import ugettext_lazy as _

from .db.base import (
    AbstractBaseModel
)


class CardManagement(AbstractBaseModel):
    """
    カード管理テーブル
        顧客:カード=1:1
    """

    customer_id = models.AutoField(
        _('Customer Id'),
        primary_key=True,
        editable=False,
    )

    total_point = models.IntegerField(
        _('Total Point'),
        default=0,
    )

    lost_flg = models.BooleanField(
        _('Lost Flg'),
        default=False,
    )

    def __str__(self):
        return str(self.customer_id)

    class Meta:
        verbose_name_plural = 'カード管理テーブル'



class BottleManagement(AbstractBaseModel):
    """
    ボトル管理マスタ
        商品名
        開栓日
    """

    deadline = models.DateTimeField(
        _('DeadLine'),
    )
    open_date = models.DateTimeField(
        _('OpenDate'),
    )
    end_flg = models.BooleanField(
        _('End Flg'),
        default=False,
    )
    waste_flg = models.BooleanField(
        _('Wasted or not'),
        default=False
    )
    customer = models.OneToOneField(
        'crm.MCustomer',
        on_delete=models.PROTECT,
    )
    # リレーション大丈夫か
    product = models.OneToOneField(
        'crm.MProduct',
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.customer.name + ' : ' + self.product.name

    class Meta:
        verbose_name_plural = 'ボトル管理テーブル'


class SalesHeader(AbstractBaseModel):
    """
    売上ヘッダ
        会計日
        総額
        顧客(1)
        担当(n)
    """

    # on_delete要検討
    customer = models.OneToOneField(
        'crm.MCustomer',
        on_delete=models.DO_NOTHING,
    )

    # on_delete要検討
    cast = models.OneToOneField(
        'crm.MCast',
        on_delete=models.DO_NOTHING,
    )

    total_sales = models.IntegerField(
        _('Total Sales'),
    )

    total_tax_sales = models.IntegerField(
        _('Total Sales included Tax'),
    )

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = '売上ヘッダ'


class SalesDetail(AbstractBaseModel):
    """
    売上明細
    """

    # CASCADEの認識正しいか？
    header = models.ForeignKey(
        SalesHeader,
        on_delete=models.CASCADE,
    )

    product = models.OneToOneField(
        'crm.MProduct',
        on_delete=models.CASCADE,
    )

    discount_flg = models.BooleanField(
        _('Discount Flg'),
        default=False,
    )

    quantity = models.DecimalField(
        _('個数'),
        max_digits=10,
        decimal_places=2,
        default=1.00,
    )

    fixed_price = models.IntegerField(
        _('Fixed Price'),
    )

    fixed_tax_price = models.IntegerField(
        _('Fixed Price included Tax'),
    )

    def __str__(self):
        return str(self.header.id)

    class Meta:
        verbose_name_plural = '売上明細'


class BookingManagement(AbstractBaseModel):
    """
    予約情報
        開始時間
        終了時間
        席
        担当
        顧客
        キャンセルフラグ
        人数
    """

    booking_date = models.DateTimeField(
        _('Booking Date')
    )

    booking_start = models.DateTimeField(
        _('Booking Start Time')
    )

    booking_end = models.DateTimeField(
        _('Booking End Time')
    )

    customer = models.ForeignKey(
        'crm.MCustomer',
        on_delete=models.CASCADE,
    )

    cast = models.ManyToManyField(
        'crm.MCast',
        blank=True,
    )

    total_person = models.SmallIntegerField(
        _('Total Person'),
        default=1,
    )

    cancel_flg = models.BooleanField(
        _('Cancel Flg'),
        default=False,
    )

    seat = models.ForeignKey(
        'crm.MSeat',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = '予約管理テーブル'


class AttendanceManagement(AbstractBaseModel):
    """
    勤怠管理テーブル
    """
    cast = models.ForeignKey(
        'crm.MCast',
        on_delete=models.CASCADE,
    )

    date = models.DateField(
        _('Work Date'),
    )

    attend_flg = models.BooleanField(
        _('Attend Flg'),
        default=False,
    )

    start = models.DateTimeField(
        _('Start Time'),
        null=True,
        blank=True,
    )

    end = models.DateTimeField(
        _('End Time'),
        null=True,
        blank=True,
    )

    absent_flg = models.BooleanField(
        _('Absent Flg'),
        default=False,
    )

    def __str__(self):
        return self.cast.name + 'の勤怠'

    class Meta:
        verbose_name_plural = '勤怠管理テーブル'
