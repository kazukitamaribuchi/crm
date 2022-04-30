from rest_framework import serializers
from django.db.models import Q


from .models import (
    MCustomer,
    MCast,
    MRank,
    MTax,
    MProduct,
    MSeat,
)

from .sub_models import (
    CardManagement,
    BottleManagement,
    SalesHeader,
    SalesDetail,
    AttendanceManagement,
    BookingManagement,
)

from .utils import (
    utc_to_jst
)

from datetime import (
    timezone,
    datetime,
    timedelta
)


import logging
import pytz


logging.basicConfig(
    level = logging.DEBUG,
    format = '''%(levelname)s %(asctime)s %(pathname)s:%(funcName)s:%(lineno)s
    %(message)s''')


logger = logging.getLogger(__name__)




class DatetimeMixin:

    def get_created_at(self, obj):
        return utc_to_jst(obj.created_at).strftime('%Y年%m月%d日 %H時%M分')

    def get_updated_at(self, obj):
        return utc_to_jst(obj.updated_at).strftime('%Y年%m月%d日 %H時%M分')




class DynamicFieldsModelSerializer(serializers.ModelSerializer, DatetimeMixin):

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)




class CardSerializer(DynamicFieldsModelSerializer):

    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = CardManagement
        fields = [
            'customer_id',
            'total_point',
            'lost_flg',
            'created_at',
            'updated_at',
            'delete_flg',
        ]


class CustomerSerializer(DynamicFieldsModelSerializer):

    card = CardSerializer()
    first_visit = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = MCustomer
        fields = [
            'id',
            'name',
            'age',
            'birthday',
            'job',
            'company',
            'address',
            'rank',
            'card',
            'first_visit',
            'total_visit',
            'total_sales',
            'caution_flg',
            'created_at',
            'updated_at',
            'delete_flg',
        ]

    def get_first_visit(self, obj):
        return utc_to_jst(obj.updated_at).strftime('%Y年%m月%d日')


class CustomerSubSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = MCustomer
        fields = [
            'id',
            'name',
        ]



class CastSerializer(DynamicFieldsModelSerializer):

    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = MCast
        fields = [
            'id',
            'name',
            'age',
            'icon',
            'real_name',
            'real_age',
            'birthday',
            'address',
            'start_working_date',
            'total_appoint',
            'resign_flg',
            'resign_date',
            'salary',
            'created_at',
            'updated_at',
            'delete_flg',
        ]


class CastSubSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = MCast
        fields = [
            'id',
            'name',
        ]


class RankSerializer(DynamicFieldsModelSerializer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = MRank
        fields = [
            'id',
            'rank',
        ]


class TaxSerializer(DynamicFieldsModelSerializer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = MTax
        fields = [
            'id',
            'tax_rate',
        ]


class ProductSerializer(DynamicFieldsModelSerializer):

    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = MProduct
        fields = [
            'id',
            'name',
            'price',
            'category',
            'tax',
            'tax_price',
            'created_at',
            'updated_at',
            'delete_flg',
        ]


class SeatSerializer(DynamicFieldsModelSerializer):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = MSeat
        fields = [
            'id',
            'seat_type',
            'seat_no',
            'limit',
        ]



class BottleSerializer(DynamicFieldsModelSerializer):

    customer = CustomerSerializer()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    deadline = serializers.SerializerMethodField()
    open_date = serializers.SerializerMethodField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = BottleManagement
        fields = [
            'id',
            'product',
            'customer',
            'deadline',
            'open_date',
            'end_flg',
            'waste_flg',
            'created_at',
            'updated_at',
            'delete_flg',
        ]

    def get_deadline(self, obj):
        return utc_to_jst(obj.deadline).strftime('%Y年%m月%d日 %H時%M分')

    def get_open_date(self, obj):
        return utc_to_jst(obj.open_date).strftime('%Y年%m月%d日 %H時%M分')



class SalesDetailSerializer(DynamicFieldsModelSerializer):

    product = ProductSerializer()

    class Meta:
        model = SalesDetail
        fields = [
            'id',
            'product',
            'quantity',
            'fixed_price',
            'fixed_tax_price',
            'discount_flg',
        ]


class SalesSerializer(DynamicFieldsModelSerializer):

    customer = CustomerSerializer()
    cast = CastSerializer()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    sales_detail = serializers.SerializerMethodField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = SalesHeader
        fields = [
            'id',
            'customer',
            'cast',
            'total_sales',
            'total_tax_sales',
            'created_at',
            'updated_at',
            'delete_flg',
            'sales_detail',
        ]

    def get_sales_detail(self, obj):
        return SalesDetailSerializer(
            SalesDetail.objects.filter(header=obj),
            many=True
        ).data



class AttendanceSerializer(DynamicFieldsModelSerializer):

    cast = CastSerializer()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = AttendanceManagement
        fields = [
            'id',
            'cast',
            'date',
            'attend_flg',
            'start',
            'end',
            'absent_flg',
            'created_at',
            'updated_at',
            'delete_flg',
        ]


class BookingSerializer(DynamicFieldsModelSerializer):

    customer = CustomerSerializer()
    cast = CastSerializer(many=True)
    booking_date = serializers.SerializerMethodField()
    booking_start = serializers.SerializerMethodField()
    booking_end = serializers.SerializerMethodField()
    seat = SeatSerializer()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = BookingManagement
        fields = [
            'id',
            'customer',
            'cast',
            'total_person',
            'booking_date',
            'booking_start',
            'booking_end',
            'cancel_flg',
            'seat',
            'created_at',
            'updated_at',
            'delete_flg',
        ]

    def get_booking_date(self, obj):
        return utc_to_jst(obj.booking_date).strftime('%Y年%m月%d日')

    def get_booking_start(self, obj):
        return utc_to_jst(obj.booking_start).strftime('%Y年%m月%d日 %H時%M分')

    def get_booking_end(self, obj):
        return utc_to_jst(obj.booking_end).strftime('%Y年%m月%d日 %H時%M分')
