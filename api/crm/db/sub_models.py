from django.db import models
from django.utils.translation import ugettext_lazy as _

from .models import (
    MCustomer,
    MProduct,
    MSeat
)

from .base import (
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
        MCustomer,
        on_delete=models.PROTECT,
    )
    # リレーション大丈夫か
    product = models.OneToOneField(
        MProduct,
        on_delete=models.PROTECT,
    )


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
        MCustomer,
        on_delete=models.SET_NULL,
    )

    # on_delete要検討
    cast = models.OneToOneField(
        MCast,
        on_delete=models.SET_NULL,
    )

    total_sales = models.IntegerField(
        _('Total Sales'),
    )

    total_tax_sales = models.IntegerField(
        _('Total Sales included Tax'),
    )


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
        Product,
        on_delete=models.CASCADE,
    )

    discount_flg = models.BooleanField(
        _('Discount Flg'),
        default=False,
    )

    fixed_price = models.IntegerField(
        _('Fixed Price'),
    )

    fixed_tax_price = models.IntegerField(
        _('Fixed Price included Tax'),
    )


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

    customer = models.OneToOneField(
        MCustomer,
        on_delete=models.CASCADE,
    )

    cast = models.ManyToManyField(
        MCast,
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

    seat = models.OneToOneField(
        MSeat,
        on_delete=models.CASCADE,
    )


class AttendanceManagement(AbstractBaseModel):
    """
    勤怠管理テーブル
    """
    cast = models.OneToOneField(
        MCast,
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
