from django.db import models
from django.utils.translation import ugettext_lazy as _

from .db.base import (
    AbstractBaseModel
)



class CardManagement(AbstractBaseModel):
    """
    カード管理テーブル
        顧客:カード=1:1
        　カード紛失もあり得るため、カードで会員Noは管理。
          連番でカード上は0埋めで8桁とか？
    """

    customer_no = models.AutoField(
        _('会員No'),
        primary_key=True,
        editable=False,
    )

    total_point = models.IntegerField(
        _('ポイント総数'),
        default=0,
    )

    lost_flg = models.BooleanField(
        _('紛失フラグ'),
        default=False,
    )

    def __str__(self):
        return str(self.customer_no)

    class Meta:
        verbose_name_plural = 'カード管理テーブル'



class BottleManagement(AbstractBaseModel):
    """
    ボトル管理マスタ
        商品名
        開栓日
    """

    open_date = models.DateTimeField(
        _('開封日'),
    )
    deadline = models.DateTimeField(
        _('賞味期限'),
        null=True,
        blank=True,
    )
    end_flg = models.BooleanField(
        _('飲み終わったかフラグ'),
        default=False,
    )
    waste_flg = models.BooleanField(
        _('廃棄フラグ'),
        default=False
    )
    customer = models.OneToOneField(
        'crm.MCustomer',
        on_delete=models.PROTECT,
        related_name='bottle',
    )
    # リレーション大丈夫か
    product = models.ForeignKey(
        'crm.MProduct',
        on_delete=models.PROTECT,
        related_name='product'
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
        related_name='sales_header'
    )

    # on_delete要検討
    cast = models.ManyToManyField(
        'crm.MCast',
        related_name='sales_header',
    )

    total_sales = models.IntegerField(
        _('総計（税抜）'),
        default=0,
    )

    total_tax_sales = models.IntegerField(
        _('総計（税込）'),
        default=0,
    )

    def __str__(self):
        return '売上No.' + str(self.id) + ' ' + str(self.total_tax_sales) + '円'

    class Meta:
        verbose_name_plural = '売上ヘッダ'
        indexes = [
            models.Index(fields=['customer'], name='sales_header_customer_idx'),
        ]


class SalesDetail(AbstractBaseModel):
    """
    売上明細
    """

    # CASCADEの認識正しいか？
    header = models.ForeignKey(
        SalesHeader,
        on_delete=models.CASCADE,
        related_name='sales_detail'
    )

    product = models.OneToOneField(
        'crm.MProduct',
        on_delete=models.CASCADE,
        related_name='sales_detail',
    )

    # 指名の場合キャストと紐づける。
    # 複数指名の場合、誰を指名したか判別できなくなるためここで明細単位で紐づけ。
    appoint = models.ForeignKey(
        'crm.MCast',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    discount_flg = models.BooleanField(
        _('値引きフラグ'),
        default=False,
    )

    quantity = models.DecimalField(
        _('個数'),
        max_digits=10,
        decimal_places=2,
        default=1.00,
    )

    fixed_price = models.IntegerField(
        _('実価格（税抜）'),
        null=True,
        blank=True,
    )

    fixed_tax_price = models.IntegerField(
        _('実価格（税込）'),
    )

    def __str__(self):
        product_name = self.product.name
        price = str(self.fixed_tax_price)
        return '売上No.' + str(self.header.id) + ' ' + product_name + ' ' + price + '円'

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

    register_date = models.DateTimeField(
        _('予約登録日')
    )

    booking_start = models.DateTimeField(
        _('予約開始時間')
    )

    booking_end = models.DateTimeField(
        _('予約終了時間'),
        null=True,
        blank=True,
    )

    customer = models.ForeignKey(
        'crm.MCustomer',
        on_delete=models.CASCADE,
    )

    cast = models.ManyToManyField(
        'crm.MCast',
        blank=True,
        related_name='booking',
    )

    total_person = models.SmallIntegerField(
        _('予約人数'),
        default=1,
    )

    cancel_flg = models.BooleanField(
        _('キャンセルフラグ'),
        default=False,
    )

    calcel_date = models.DateTimeField(
        null=True,
        blank=True,
    )

    seat = models.ForeignKey(
        'crm.MSeat',
        on_delete=models.CASCADE,
        related_name='booking',
    )

    def __str__(self):
        start = self.booking_start.strftime('%Y年%m月%d日 %H時%M分')
        end = self.booking_end.strftime('%H時%M分') if self.booking_end != None else ''
        return self.customer.name + '様 ' + start + '~' + end

    class Meta:
        verbose_name_plural = '予約管理テーブル'


class AttendanceManagement(AbstractBaseModel):
    """
    勤怠管理テーブル
    """
    cast = models.ForeignKey(
        'crm.MCast',
        on_delete=models.CASCADE,
        related_name='attendance',
    )

    start = models.DateTimeField(
        _('勤務開始時間'),
    )

    end = models.DateTimeField(
        _('勤務終了時間'),
        null=True,
        blank=True,
    )

    late_flg = models.BooleanField(
        _('遅刻フラグ'),
        default=False,
    )

    attend_flg = models.BooleanField(
        _('出勤フラグ'),
        default=False,
    )

    absent_flg = models.BooleanField(
        _('欠勤フラグ'),
        default=False,
    )

    def __str__(self):
        attend = '〇' if self.attend_flg else '×'
        return self.cast.name + ' ' + self.date.strftime('%Y年%m月%d日') + '→' + attend

    class Meta:
        verbose_name_plural = '勤怠管理テーブル'
        indexes = [
            models.Index(fields=['cast'], name='attendance_cast_idx'),
        ]
