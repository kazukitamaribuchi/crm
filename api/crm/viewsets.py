from rest_framework import (
    generics,
    permissions,
    authentication,
    status,
    viewsets,
    filters,
)

from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum, Q

from datetime import (
    datetime,
)

from .serializers import (
    CustomerSerializer,
    CastSerializer,
    RankSerializer,
    TaxSerializer,
    ProductSerializer,
    SeatSerializer,
    CardSerializer,
    BottleSerializer,
    SalesSerializer,
    AttendanceSerializer,
    BookingSerializer,
)

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

from .exceptions import (
    WrongUserException
)

import logging

logger = logging.getLogger(__name__)

PRODUCT_CATEGORY = {
    0: [0,1,2,3,4],
    1: {
        0: [0,1,2,3,4,5,6],
        1: [],
        2: [],
    },
    2: [0,1,2,3,4],
}




class BaseModelViewSet(viewsets.ModelViewSet):
    """
    """


class CustomerViewSet(BaseModelViewSet):
    """
    """
    permission_classes = (permissions.AllowAny,)
    queryset = MCustomer.objects.all()
    serializer_class = CustomerSerializer

    def create(self, request, *args, **kwargs):
        """
        顧客作成
        　・必須項目
            custoner_no(CardManagement) => カードNoは渡したカードのNo

            name
            name_kana
            age
            birthday
            job
            company

            ※後は要望に応じて
        """

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(self.get_serializer(serializer.instance).data,
                status=status.HTTP_201_CREATED)

        logger.debug(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, pk=None):
        logger.debug("★UPDATE")
        logger.debug(request.data)
        logger.debug(request.data['id'])

        queryset = self.queryset.get(pk=pk)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




        # try:
        #     customer = MCustomer.objects.get(pk=request.data['id'])
        # except MCustomer.DoesNotExist:
        #     return
        #
        # # 会員Noが正しいか
        # # ・誰とも紐づいていない会員NoだったらOK。自分だったらそのまま
        #
        # customer_no = request.data['customer_no']
        #
        # try:
        #     card_user = MCustomer.objects.get(card__customer_no=customer_no)
        #     if card_user != customer:
        #         raise WrongUserException
        # except WrongUserException:
        #     logger.error('既に他のユーザーと紐づいているカードなのでNG')
        # except MCustomer.DoesNotExist:
        #     logger.debug('顧客情報が見つからないので新たに紐づけ直す')
        # else:
        #     logger.debug('会員Noはそのまま')
        #
        #
        #
        # # 該当会員Noを持った顧客の取得
        # #  MCustomer.objects.get(card__customer_no=1)
        # # 該当会員Noのカードを取得
        # #  CardManagement.objects.get(customer_no=1).customer
        #
        # # ★変わった項目のみ更新したい・・・
        # customer.name = request.data['name']
        # customer.name_kana = request.data['name_kana']
        # customer.age = request.data['age']
        # customer.birthday = datetime.strptime(request.data['birthday'], '%Y-%m-%d')
        # customer.job = request.data['job']
        # customer.company = request.data['company']
        # customer.age = request.data['age']
        # customer.age = request.data['age']
        # customer.save()
        #
        # return Response(self.get_serializer(customer).data, status=status.HTTP_200_OK)


class RankViewSet(BaseModelViewSet):
    """
    """
    permission_classes = (permissions.AllowAny,)
    queryset = MRank.objects.all()
    serializer_class = RankSerializer


class TaxViewSet(BaseModelViewSet):
    """
    """
    permission_classes = (permissions.AllowAny,)
    queryset = MTax.objects.all()
    serializer_class = TaxSerializer


class CastViewSet(BaseModelViewSet):
    """
    """
    permission_classes = (permissions.AllowAny,)
    queryset = MCast.objects.all()
    serializer_class = CastSerializer


class ProductViewSet(BaseModelViewSet):
    """
    """
    permission_classes = (permissions.AllowAny,)
    queryset = MProduct.objects.all()
    serializer_class = ProductSerializer

    @action(methods=['get'], detail=False)
    def get_product_by_category(self, request):
        """
        カテゴリ毎の商品を取得。
        マスタデータになるため、画面側のlocalStorageに持つ。
        """

        res = {
            0: {},
            1: {
                0: {},
                1: [],
                2: [],
            },
            2: {},
        }

        for large, items in PRODUCT_CATEGORY.items():
            for middle in items:
                if large == 0:
                    q = MProduct.objects.get(Q(category__large_category=large), \
                            Q(category__middle_category=middle))
                    data = ProductSerializer(q).data
                    logger.debug(data)

                    res[large][middle] = data

                if large == 1:
                    if middle == 0:
                        for key in items:
                            for small in items[key]:
                                # logger.debug(str(large) + str(middle) + str(small))
                                q = MProduct.objects.filter(Q(category__large_category=large), \
                                        Q(category__middle_category=middle), \
                                        Q(category__small_category=small))
                                data = ProductSerializer(q, many=True).data
                                res[large][middle][small] = data

                if large == 2:
                    q = MProduct.objects.filter(Q(category__large_category=large), \
                            Q(category__middle_category=middle))
                    data = ProductSerializer(q, many=True).data
                    res[large][middle] = data


        return Response(res, status=status.HTTP_200_OK)



class SeatViewSet(BaseModelViewSet):
    """
    """
    permission_classes = (permissions.AllowAny,)
    queryset = MSeat.objects.all()
    serializer_class = SeatSerializer


class CardViewSet(BaseModelViewSet):
    """
    """
    permission_classes = (permissions.AllowAny,)
    queryset = CardManagement.objects.all()
    serializer_class = CardSerializer


class BottleViewSet(BaseModelViewSet):
    """
    """
    permission_classes = (permissions.AllowAny,)
    queryset = BottleManagement.objects.all()
    serializer_class = BottleSerializer


class SalesViewSet(BaseModelViewSet):
    """
    """
    permission_classes = (permissions.AllowAny,)
    queryset = SalesHeader.objects.all()
    serializer_class = SalesSerializer


class BookingViewSet(BaseModelViewSet):
    """
    """
    permission_classes = (permissions.AllowAny,)
    queryset = BookingManagement.objects.all()
    serializer_class = BookingSerializer


class AttendanceViewSet(BaseModelViewSet):
    """
    """
    permission_classes = (permissions.AllowAny,)
    queryset = AttendanceManagement.objects.all()
    serializer_class = AttendanceSerializer
