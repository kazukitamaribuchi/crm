from rest_framework import serializers
from django.db.models import Q


from .models import (
    MCustomer,
    MCast,
    MRank,
    MTax,
    MProduct,
    MProductCategory,
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
    utc_to_jst,
    users_card,
    other_users_card,
    get_card_user,
    get_val_in_validated_data,
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
        if obj.created_at == None:
            return ''
        return utc_to_jst(obj.created_at).strftime('%Y/%m/%d %H:%M')

    def get_updated_at(self, obj):
        if obj.updated_at == None:
            return ''
        return utc_to_jst(obj.updated_at).strftime('%Y/%m/%d %H:%M')




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
            'customer_no',
            'total_point',
            'lost_flg',
            'created_at',
            'updated_at',
            'delete_flg',
        ]

class RankSerializer(DynamicFieldsModelSerializer):

    # customer = serializers.StringRelatedField(many=True)
    customer = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
    )

    class Meta:
        model = MRank
        fields = [
            'rank_id',
            'rank_name',
            'customer'
        ]


class CustomerSerializer(DynamicFieldsModelSerializer):

    # card = CardSerializer()
    first_visit = serializers.SerializerMethodField(allow_null=True)
    birthday = serializers.SerializerMethodField(allow_null=True)
    birthday_str = serializers.CharField(write_only=True, allow_blank=True)
    job = serializers.SerializerMethodField(default='', allow_null=True)
    company = serializers.SerializerMethodField(default='', allow_null=True)
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    total_visit = serializers.IntegerField(default=0, allow_null=True)
    total_sales = serializers.IntegerField(default=0, allow_null=True)
    customer_no = serializers.IntegerField(source='card.customer_no', allow_null=True)
    delete_flg = serializers.BooleanField(default=False)
    caution_flg = serializers.BooleanField(default=False)

    rank_id = serializers.IntegerField(source='rank.rank_id', allow_null=True)
    rank_name = serializers.CharField(
        source='rank.rank_name',
        read_only=True,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = MCustomer
        fields = [
            'id',
            'name',
            'name_kana',
            'age',
            'birthday',
            'birthday_str',
            'job',
            'company',
            'address',
            'rank_id',
            'rank_name',
            # 'card',
            'first_visit',
            'total_visit',
            'total_sales',
            'caution_flg',
            'created_at',
            'updated_at',
            'delete_flg',
            'customer_no',
        ]

    def get_first_visit(self, obj):
        if obj.first_visit == None:
            return ''
        return utc_to_jst(obj.first_visit).strftime('%Y/%m/%d')

    def get_birthday(self, obj):
        if obj.birthday == None:
            return ''
        return obj.birthday.strftime('%Y/%m/%m')

    def get_job(self, obj):
        if obj.job == None:
            return ''
        return obj.job

    def get_company(self, obj):
        if obj.company == None:
            return ''
        return obj.company

    def get_address(self, obj):
        if obj.company == None:
            return ''
        return obj.company

    def create(self, validated_data):
        logger.debug('★Serializerのcreate')
        logger.debug(validated_data)


        if users_card(validated_data['card']['customer_no']):
            return None

        try:
            rank = MRank.objects.get(
                rank_id = validated_data['rank']['rank_id']
            )
        except MRank.DoesNotExist:
            logger.error('存在しないランクIDです。')
            return None

        card, c_created = CardManagement.objects.get_or_create(
            customer_no = validated_data['card']['customer_no']
        )

        birthday_str = get_val_in_validated_data('birthday_str', validated_data)
        birthday = datetime.strptime(birthday_str, '%Y/%m/%d') if birthday_str != '' else None
        job = get_val_in_validated_data('job', validated_data)
        company = get_val_in_validated_data('company', validated_data)

        customer = MCustomer.objects.create(
            name=validated_data['name'],
            name_kana=validated_data['name_kana'],
            age=validated_data['age'],
            birthday=birthday,
            job=job,
            company=company,
            caution_flg=validated_data['caution_flg'],
            rank=rank,
            card=card,
        )

        return customer

    def update(self, instance, validated_data):
        logger.debug('★Serializerのupdate')
        logger.debug(instance)
        logger.debug(validated_data)

        card_user = get_card_user(validated_data['card']['customer_no'])
        if card_user != None and card_user != instance:
            logger.debug(card_user)
            logger.debug(instance)
            logger.error('既に他のユーザーと紐づいているカードです。')
            return None

        try:
            rank = MRank.objects.get(
                rank_id = validated_data['rank']['rank_id']
            )
        except MRank.DoesNotExist:
            logger.error('存在しないランクIDです。')
            return None

        card, c_created = CardManagement.objects.get_or_create(
            customer_no = validated_data['card']['customer_no']
        )

        birthday_str = get_val_in_validated_data('birthday_str', validated_data)
        birthday = datetime.strptime(birthday_str, '%Y/%m/%d') if birthday_str != '' else None
        job = get_val_in_validated_data('job', validated_data)
        company = get_val_in_validated_data('company', validated_data)

        instance.name = validated_data['name']
        instance.name_kana = validated_data['name_kana']
        instance.age = validated_data['age']
        instance.birthday = birthday
        instance.job = job
        instance.company = company
        instance.card = card
        instance.rank = rank
        instance.save()
        return instance


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



class TaxSerializer(DynamicFieldsModelSerializer):

    product = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
    )

    class Meta:
        model = MTax
        fields = [
            'id',
            'tax_rate',
            'product',
        ]


class ProductCategorySerializer(DynamicFieldsModelSerializer):

    LARGE_CATEGORIES = {
        # 0: '基本料金',
        1: '飲料',
        2: 'フード'
    }

    CATEGORIES = {
        # 0: {
        #     0: '基本料金',
        #     1: '指名料',
        #     2: '場内指名料',
        #     3: 'VIP料金',
        #     4: '同伴料金',
        # },
        1: {
            0: [
                'アルコール',
                {
                    0: 'シャンパン',
                    1: 'ワイン',
                    2: '焼酎',
                    3: 'サワー',
                    4: 'カクテル',
                    5: '日本酒',
                    6: 'ビール',
                },
            ],
            1: 'ノンアルコール',
            2: 'ソフトドリンク',
        },
        2: {
            0: 'メイン',
            1: 'サラダ',
            2: 'おかず',
            3: 'おつまみ',
            4: 'デザート',
        }
    }

    large_category_label = serializers.SerializerMethodField()
    middle_category_label = serializers.SerializerMethodField()
    small_category_label = serializers.SerializerMethodField()

    class Meta:
        model = MProductCategory
        fields = [
            'id',
            'large_category',
            'middle_category',
            'small_category',
            'large_category_label',
            'middle_category_label',
            'small_category_label',
        ]

    def get_large_category_label(self, obj):
        return self.LARGE_CATEGORIES[obj.large_category]

    def get_middle_category_label(self, obj):
        # logger.debug('large' + str(obj.large_category))
        # logger.debug('middle' + str(obj.middle_category))
        # logger.debug('small' + str(obj.small_category))
        if obj.large_category == 1 and obj.middle_category == 0:
            return self.CATEGORIES[obj.large_category][obj.middle_category][0]
        return self.CATEGORIES[obj.large_category][obj.middle_category]

    def get_small_category_label(self, obj):
        if obj.large_category == 1 and obj.middle_category == 0:
            return self.CATEGORIES[obj.large_category][obj.middle_category][1][obj.small_category]
        return 'なし'


class ProductSerializer(DynamicFieldsModelSerializer):

    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    category = ProductCategorySerializer()
    tax = TaxSerializer(fields=['id', 'tax_rate'])

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
            'thumbnail',
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
    product = ProductSerializer()

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
        if obj.deadline == None:
            return ''
        return utc_to_jst(obj.deadline).strftime('%Y年%m月%d日 %H時%M分')

    def get_open_date(self, obj):
        if obj.open_date == None:
            return ''
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
    cast = CastSerializer(many=True)
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
    start = serializers.SerializerMethodField()
    end = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = AttendanceManagement
        fields = [
            'id',
            'cast',
            'attend_flg',
            'start',
            'end',
            'absent_flg',
            'late_flg',
            'created_at',
            'updated_at',
            'delete_flg',
        ]


    def get_start(self, obj):
        if obj.start == None:
            return ''
        return utc_to_jst(obj.start).strftime('%Y年%m月%d日 %H時%M分')

    def get_end(self, obj):
        if obj.end == None:
            return ''
        return utc_to_jst(obj.end).strftime('%Y年%m月%d日 %H時%M分')


class BookingSerializer(DynamicFieldsModelSerializer):

    customer = CustomerSerializer()
    cast = CastSerializer(many=True)
    register_date = serializers.SerializerMethodField()
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
            'register_date',
            'booking_start',
            'booking_end',
            'cancel_flg',
            'seat',
            'created_at',
            'updated_at',
            'delete_flg',
        ]

    def get_register_date(self, obj):
        if obj.register_date == None:
            return ''
        return utc_to_jst(obj.register_date).strftime('%Y年%m月%d日')

    def get_booking_start(self, obj):
        if obj.booking_start == None:
            return ''
        return utc_to_jst(obj.booking_start).strftime('%Y年%m月%d日 %H時%M分')

    def get_booking_end(self, obj):
        if obj.booking_end == None:
            return ''
        return utc_to_jst(obj.booking_end).strftime('%Y年%m月%d日 %H時%M分')
