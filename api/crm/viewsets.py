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
from django.db import transaction
from django.db.models import Sum, Q

from datetime import (
    datetime,
    timedelta,
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
    QuestionSerializer,
)

from .models import (
    MCustomer,
    MCast,
    MRank,
    MTax,
    MProduct,
    MSeat,
    MPayment,
    MService,
    MQuestion,
)

from .sub_models import (
    CardManagement,
    BottleManagement,
    SalesHeader,
    SalesDetail,
    SalesServiceDetail,
    SalesAppointDetail,
    AttendanceManagement,
    BookingManagement,
    QuestionAnswer,
)

from .exceptions import (
    WrongUserException
)

from .utils import (
    utc_to_jst,
    users_card,
)


import logging

logger = logging.getLogger(__name__)

PRODUCT_CATEGORY = {
    # 基本料金は別で管理
    # 0: [0,1,2,3,4],

    1: {
        # アルコール
        0: [0,1,2,3,4,5,6],

        # ノンアル
        1: [0],

        # ソフトドリンク
        2: [0],
    },
    # 2: [0,1,2,3,4],
    2: {
        # メイン => 和食、洋食、ファーストフード的な?
        0: [0],
        # サラダ
        1: [0],
        # 前菜
        2: [0],
        # 揚げ物
        3: [0],
        # 吸い物、御飯物
        4: [0],
    }
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

    @action(methods=['post'], detail=False)
    def get_customer_no_duplicate(self, request):
        """
        顧客Noが重複していないかのチェック
        """
        logger.debug(request.data)
        logger.debug(request.query_params)
        customer_no = request.data['customer_no']

        if users_card(customer_no):
            return Response({
                'status': 'success',
                'result': False,
                'msg': '既に他のユーザーと紐づいているカードです'
            }, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'success', 'result': True}, status=status.HTTP_200_OK)


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

class QuestionViewSet(BaseModelViewSet):
    """
    """
    permission_classes = (permissions.AllowAny,)
    queryset = MQuestion.objects.all()
    serializer_class = QuestionSerializer


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
            1: {
                0: {},
                1: {},
                2: {},
            },
            2: {
                0: {},
                1: {},
                2: {},
                3: {},
            },
        }

        for large, items in PRODUCT_CATEGORY.items():
            for middle in items:
                for small in items[middle]:
                    q = MProduct.objects.filter(Q(category__large_category=large), \
                        Q(category__middle_category=middle), \
                        Q(category__small_category=small)
                    )
                    data = ProductSerializer(q, many=True).data
                    # logger.debug('large=> ' + str(large) + ' middle=> ' + str(middle) + ' small=> ' + str(small))
                    res[large][middle][small] = data

        return Response(res, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False)
    def get_popular_product(self, request):
        """
        人気商品を取得
        　・明細追加時のトップに表示
            それぞれのタブ毎に表示するためなど

            トップ
            アルコール、ノンアルコール、ソフトドリンク
            メイン、サラダ、おかず、おつまみ、デザート
        """

        # 人気商品の算出ロジックは後で。とりあえず固定で

        try:
            res = MProduct.objects.all()[:12]
            top = {
                0: ProductSerializer(MProduct.objects.filter(category__large_category=1, category__middle_category=0)[:12], many=True).data,
                1: ProductSerializer(MProduct.objects.filter(category__large_category=1, category__middle_category=1)[:12], many=True).data,
                2: ProductSerializer(MProduct.objects.filter(category__large_category=1, category__middle_category=2)[:12], many=True).data,
                3: ProductSerializer(MProduct.objects.filter(category__large_category=2, category__middle_category=0)[:12], many=True).data,
                4: ProductSerializer(MProduct.objects.filter(category__large_category=2, category__middle_category=1)[:12], many=True).data,
                5: ProductSerializer(MProduct.objects.filter(category__large_category=2, category__middle_category=2)[:12], many=True).data,
                6: ProductSerializer(MProduct.objects.filter(category__large_category=2, category__middle_category=3)[:12], many=True).data,
            }
            return Response({
                'status': 'success',
                'data': {
                    'popular': ProductSerializer(res, many=True).data,
                    'top': top,
                }
            }, status=status.HTTP_200_OK)
        except:
            import traceback
            traceback.print_exc()
            return Response({'status': 'error'}, status=status.HTTP_400_BAD_REQUEST)


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

    @transaction.atomic
    @action(methods=['post'], detail=False)
    def create_sales_data(self, request):

        logger.debug('★create_sales_data')
        logger.debug(request.data)

        customer_no = request.data['customer_no']
        try:
            customer = MCustomer.objects.get(card__customer_no=customer_no)
        except MCustomer.DoesNotExist:
            logger.error('顧客情報が取得出来ません。')
            return Response(status.status.HTTP_400_BAD_REQUEST)

        account_date_str = request.data['account_date']
        account_date = datetime.strptime(account_date_str, '%Y-%m-%d')

        visit_time_str = request.data['visit_time']
        visit_time = datetime.strptime(visit_time_str, '%Y-%m-%d %H:%M')
        leave_time_str = request.data['leave_time']
        leave_time = datetime.strptime(leave_time_str, '%Y-%m-%d %H:%M')
        move_time = datetime.strptime(request.data['move_time'], '%Y-%m-%d %H:%M')  if request.data['move_time'] != None else None

        type = request.data['payment_type']
        payment = MPayment.objects.get(type=0)
        logger.debug(type)
        try:
            payment = MPayment.objects.get(type=type)
        except:
            logger.error('支払い方法が取得出来ません')

        appoint = request.data['appoint']
        # 後々
        booking = False

        basic_plan_type = request.data['basic_plan_type']
        stay_hour = request.data['stay_hour']
        stay_hour_other = request.data['stay_hour_other']
        total_stay_hour = request.data['total_stay_hour']

        total_sales = request.data['total_sales']
        total_tax_sales = request.data['total_tax_sales']


        header = SalesHeader.objects.create(
            customer=customer,
            payment=payment,
            appoint=appoint,
            booking=booking,
            basic_plan_type=basic_plan_type,
            stay_hour=stay_hour,
            stay_hour_other=stay_hour_other,
            total_stay_hour=total_stay_hour,
            total_sales=total_sales,
            total_tax_sales=total_tax_sales,
            visit_time=visit_time,
            leave_time=leave_time,
            account_date=account_date
        )

        sales_service_detail_list = []
        sales_appoint_detail_list = []
        sales_detail_list = []

        for data in request.data['sales_detail_service_list']:
            logger.debug('★★')
            logger.debug(data)
            service = MService.objects.get(
                basic_plan_type=data['basic_plan_type'],
                large_category=data['large_category'],
                middle_category=data['middle_category'],
            )

            # 基本料金なのでcastはNone
            cast = None

            sales_service_detail_list.append(
                SalesServiceDetail(
                    header=header,
                    service=service,
                    cast=cast,
                    quantity=data['quantity'],
                    fixed_price=data['fixed_price'],
                    fixed_tax_price=data['fixed_tax_price'],
                    total_price=data['total_price'],
                    total_tax_price=data['total_tax_price'],
                )
            )

        for data in request.data['sales_detail_appoint_list']:
            logger.debug('★★★')
            logger.debug(data)
            service = MService.objects.get(
                basic_plan_type=data['basic_plan_type'],
                large_category=data['large_category'],
                middle_category=data['middle_category'],
            )

            # 指名、同伴の場合キャストが紐づく
            cast = None
            if data['large_category'] == 1 or data['large_category'] == 2:
                cast = MCast.objects.get(id=data['cast_id'])

            sales_appoint_detail_list.append(
                SalesAppointDetail(
                    header=header,
                    service=service,
                    cast=cast,
                    quantity=data['quantity'],
                    fixed_price=data['fixed_price'],
                    fixed_tax_price=data['fixed_tax_price'],
                    total_price=data['total_price'],
                    total_tax_price=data['total_tax_price'],
                )
            )



        for data in request.data['sales_detail_list']:
            logger.debug('★★★★')
            logger.debug(data)
            try:
                product = MProduct.objects.get(id=data['product_id'])
            except:
                logger.error('商品が取得出来ません')

            # これは誰が頼ませた商品か判別させるもの
            cast = None
            try:
                cast = MCast.objects.get(id=data['cast_id'])
            except:
                logger.error('キャストが取得出来ません')

            # ボトル登録フラグ立ってたらボトル登録
            if data['bottle']:
                pass

            logger.debug('＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿')

            sales_detail_list.append(
                SalesDetail(
                    header=header,
                    product=product,
                    cast=cast,
                    quantity=data['quantity'],
                    fixed_price=data['fixed_price'],
                    fixed_tax_price=data['fixed_tax_price'],
                    total_price=data['total_price'],
                    total_tax_price=data['total_tax_price'],
                )
            )

        logger.debug('★★★★★★最終局面★★★★★★')

        if len(sales_service_detail_list) > 0:
            SalesServiceDetail.objects.bulk_create(sales_service_detail_list)
        if len(sales_appoint_detail_list) > 0:
            SalesAppointDetail.objects.bulk_create(sales_appoint_detail_list)
        if len(sales_detail_list) > 0:
            SalesDetail.objects.bulk_create(sales_detail_list)

        customer.total_visit = customer.total_visit + 1
        customer.total_sales = customer.total_sales + total_tax_sales

        if customer.first_visit == None:
            customer.first_visit = account_date

        customer.save()

        return Response(SalesSerializer(header).data, status=status.HTTP_201_CREATED)


class BookingViewSet(BaseModelViewSet):
    """
    """
    permission_classes = (permissions.AllowAny,)
    queryset = BookingManagement.objects.all()
    serializer_class = BookingSerializer

    # def list(self, request):
    #     queryset =


class AttendanceViewSet(BaseModelViewSet):
    """
    """
    permission_classes = (permissions.AllowAny,)
    queryset = AttendanceManagement.objects.all()
    serializer_class = AttendanceSerializer
