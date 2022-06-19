from rest_framework import (
    generics,
    permissions,
    authentication,
    status,
    viewsets,
    filters,
)

from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import transaction, models
from django.db.models import Sum, Q

from datetime import (
    datetime,
    timedelta,
)

from pytz import timezone

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
    CustomerSalesSerializer,
    ProductSalesSerializer,
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

OPEN_HOUR = 20
OPEN_MINUTE = 30
CLOSE_HOUR = 7
CLOSE_MINUTE = 0



class BaseModelViewSet(viewsets.ModelViewSet):
    """
    """


class CustomerViewSet(BaseModelViewSet):
    """
    """
    # permission_classes = (permissions.IsAuthenticated,)
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
        logger.debug(serializer)
        logger.debug(serializer.is_valid())
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


    @action(methods=['get'], detail=False)
    def get_customer_age(self, request):

        res = [
            MCustomer.objects.filter(age__gte=bottom*10+10, age__lte=top).count() for bottom, top in enumerate(range(19, 90, 10))
        ]

        return Response({'status': 'success', 'data': res}, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False)
    def get_customer_rank(self, request):

        res = [
            MCustomer.objects.filter(rank=rank).count() for rank in range(1, 6)
        ]

        return Response({'status': 'success', 'data': res}, status=status.HTTP_200_OK)


class RankViewSet(BaseModelViewSet):
    """
    """
    permission_classes = (permissions.IsAuthenticated,)
    queryset = MRank.objects.all()
    serializer_class = RankSerializer


class TaxViewSet(BaseModelViewSet):
    """
    """
    permission_classes = (permissions.IsAuthenticated,)
    queryset = MTax.objects.all()
    serializer_class = TaxSerializer

class QuestionViewSet(BaseModelViewSet):
    """
    """
    permission_classes = (permissions.IsAuthenticated,)
    queryset = MQuestion.objects.all()
    serializer_class = QuestionSerializer


class CastViewSet(BaseModelViewSet):
    """
    """
    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (permissions.AllowAny,)
    queryset = MCast.objects.all()
    serializer_class = CastSerializer

    def create(self, request, *args, **kwargs):
        """
        キャスト作成
        　・必須項目
            name
            age

            ※後は要望に応じて
        """

        logger.debug('★キャスト作成')
        logger.debug(request.data)

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
        logger.debug(serializer)
        logger.debug(serializer.is_valid())
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False)
    def get_cast_avg_age(self, request):

        res = MCast.objects.aggregate(avg=models.Avg('age'))

        return Response({'status': 'success', 'data': res}, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False)
    def get_cast_age(self, request):

        res = [
            MCast.objects.filter(age__lt=20).count(),
            MCast.objects.filter(age__gte=20, age__lt=25).count(),
            MCast.objects.filter(age__gte=25, age__lt=30).count(),
            MCast.objects.filter(age__gte=30, age__lt=35).count(),
            MCast.objects.filter(age__gte=35, age__lt=40).count(),
            MCast.objects.filter(age__gte=40).count(),
        ]

        return Response({'status': 'success', 'data': res}, status=status.HTTP_200_OK)



class ProductViewSet(BaseModelViewSet):
    """
    """
    # permission_classes = (permissions.IsAuthenticated,)
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
                4: {},
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
            res = MProduct.objects.filter(delete_flg=False)[:12]
            top = {
                0: ProductSerializer(MProduct.objects.filter(category__large_category=1, category__middle_category=0)[:12], many=True).data,
                1: ProductSerializer(MProduct.objects.filter(category__large_category=1, category__middle_category=1)[:12], many=True).data,
                2: ProductSerializer(MProduct.objects.filter(category__large_category=1, category__middle_category=2)[:12], many=True).data,
                3: ProductSerializer(MProduct.objects.filter(category__large_category=2, category__middle_category=0)[:12], many=True).data,
                4: ProductSerializer(MProduct.objects.filter(category__large_category=2, category__middle_category=1)[:12], many=True).data,
                5: ProductSerializer(MProduct.objects.filter(category__large_category=2, category__middle_category=2)[:12], many=True).data,
                6: ProductSerializer(MProduct.objects.filter(category__large_category=2, category__middle_category=3)[:12], many=True).data,
                7: ProductSerializer(MProduct.objects.filter(category__large_category=2, category__middle_category=4)[:12], many=True).data,
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
    permission_classes = (permissions.IsAuthenticated,)
    queryset = MSeat.objects.all()
    serializer_class = SeatSerializer


class CardViewSet(BaseModelViewSet):
    """
    """
    permission_classes = (permissions.IsAuthenticated,)
    queryset = CardManagement.objects.all()
    serializer_class = CardSerializer


class BottleViewSet(BaseModelViewSet):
    """
    """
    permission_classes = (permissions.IsAuthenticated,)
    queryset = BottleManagement.objects.all()
    serializer_class = BottleSerializer


class SalesViewSet(BaseModelViewSet):
    """
    """
    # permission_classes = (permissions.IsAuthenticated,)
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
        account_date = datetime.strptime(account_date_str, '%Y-%m-%d').astimezone(timezone('Asia/Tokyo'))

        visit_time_str = request.data['visit_time']
        visit_time = datetime.strptime(visit_time_str, '%Y-%m-%d %H:%M').astimezone(timezone('Asia/Tokyo'))
        leave_time_str = request.data['leave_time']
        leave_time = datetime.strptime(leave_time_str, '%Y-%m-%d %H:%M').astimezone(timezone('Asia/Tokyo'))
        move_diff_seat = request.data['move_diff_seat']

        move_time_str = request.data['move_time']
        move_time = datetime.strptime(move_time_str, '%Y-%m-%d %H:%M').astimezone(timezone('Asia/Tokyo'))  if move_diff_seat else None

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

        is_charterd = request.data['is_charterd']
        tax_rate = request.data['tax_rate']
        total_visitors = request.data['total_visitors']
        remarks = request.data['remarks']

        header = SalesHeader.objects.create(
            customer=customer,
            payment=payment,
            appoint=appoint,
            total_visitors=total_visitors,
            is_charterd=is_charterd,
            tax_rate=tax_rate,
            booking=booking,
            move_diff_seat=move_diff_seat,
            basic_plan_type=basic_plan_type,
            stay_hour=stay_hour,
            stay_hour_other=stay_hour_other,
            total_stay_hour=total_stay_hour,
            total_sales=total_sales,
            total_tax_sales=total_tax_sales,
            visit_time=visit_time,
            leave_time=leave_time,
            move_time=move_time,
            account_date=account_date,
            remarks=remarks,
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
            # ★開封日は会計日で良いか？
            if data['bottle']:
                BottleManagement.objects.create(
                    customer=customer,
                    product=product,
                    open_date=account_date
                )
                logger.debug('★ボトル登録 : ' + customer.name)

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
                    remarks=data['remarks'],
                )
            )

        logger.debug('★★★★★★最終局面★★★★★★')

        if len(sales_service_detail_list) > 0:
            SalesServiceDetail.objects.bulk_create(sales_service_detail_list)
        if len(sales_appoint_detail_list) > 0:
            SalesAppointDetail.objects.bulk_create(sales_appoint_detail_list)
        if len(sales_detail_list) > 0:
            SalesDetail.objects.bulk_create(sales_detail_list)

        return Response(SalesSerializer(header).data, status=status.HTTP_201_CREATED)

    @transaction.atomic
    @action(methods=['put'], detail=False)
    def update_sales_data(self, request):

        logger.debug('★update_sales_data')
        logger.debug(request.data)

        sales_header_id = request.data['id']

        customer_no = request.data['customer_no']
        try:
            customer = MCustomer.objects.get(card__customer_no=customer_no)
        except MCustomer.DoesNotExist:
            logger.error('顧客情報が取得出来ません。')
            return Response(status.status.HTTP_400_BAD_REQUEST)

        account_date_str = request.data['account_date']
        account_date = datetime.strptime(account_date_str, '%Y-%m-%d').astimezone(timezone('Asia/Tokyo'))

        visit_time_str = request.data['visit_time']
        visit_time = datetime.strptime(visit_time_str, '%Y-%m-%d %H:%M').astimezone(timezone('Asia/Tokyo'))
        leave_time_str = request.data['leave_time']
        leave_time = datetime.strptime(leave_time_str, '%Y-%m-%d %H:%M').astimezone(timezone('Asia/Tokyo'))
        move_diff_seat = request.data['move_diff_seat']

        move_time_str = request.data['move_time']
        move_time = datetime.strptime(move_time_str, '%Y-%m-%d %H:%M').astimezone(timezone('Asia/Tokyo'))  if move_diff_seat else None

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

        is_charterd = request.data['is_charterd']
        tax_rate = request.data['tax_rate']
        total_visitors = request.data['total_visitors']
        remarks = request.data['remarks']

        try:
            header = SalesHeader.objects.get(id=sales_header_id)
        except:
            logger.error('売上ヘッダーを取得出来ません')

        header.customer = customer
        header.payment = payment
        header.appoint = appoint
        header.total_visitors = total_visitors
        header.is_charterd = is_charterd
        header.tax_rate = tax_rate
        header.booking = booking
        header.move_diff_seat = move_diff_seat
        header.basic_plan_type = basic_plan_type
        header.stay_hour = stay_hour
        header.stay_hour_other = stay_hour_other
        header.total_sales = total_sales
        header.total_tax_sales = total_tax_sales
        header.visit_time = visit_time
        header.leave_time = leave_time
        header.move_time = move_time
        header.account_date = account_date
        header.remarks = remarks

        # header = SalesHeader.objects.create(
        #     customer=customer,
        #     payment=payment,
        #     appoint=appoint,
        #     total_visitors=total_visitors,
        #     is_charterd=is_charterd,
        #     tax_rate=tax_rate,
        #     booking=booking,
        #     move_diff_seat=move_diff_seat,
        #     basic_plan_type=basic_plan_type,
        #     stay_hour=stay_hour,
        #     stay_hour_other=stay_hour_other,
        #     total_stay_hour=total_stay_hour,
        #     total_sales=total_sales,
        #     total_tax_sales=total_tax_sales,
        #     visit_time=visit_time,
        #     leave_time=leave_time,
        #     move_time=move_time,
        #     account_date=account_date,
        #     remarks=remarks,
        # )

        header.save()

        edit_sales_detail = request.data['edit_sales_detail']
        edit_sales_service_detail = request.data['edit_sales_service_detail']
        edit_sales_appoint_detail = request.data['edit_sales_appoint_detail']

        logger.debug('明細の削除')
        logger.debug(edit_sales_detail)
        logger.debug(edit_sales_service_detail)
        logger.debug(edit_sales_appoint_detail)

        for item in edit_sales_detail:
            try:
                salesDetail = SalesDetail.objects.get(id=item['id'])
                salesDetail.delete()
            except:
                logger.error('salesDetail id => ' + item['id'])

        for item in edit_sales_service_detail:
            try:
                salesServiceDetail = SalesServiceDetail.objects.get(id=item['id'])
                salesServiceDetail.delete()
            except:
                logger.error('salesServiceDetail id => ' + item['id'])

        for item in edit_sales_appoint_detail:
            try:
                salesAppointDetail = SalesAppointDetail.objects.get(id=item['id'])
                salesAppointDetail.delete()
            except:
                logger.error('salesAppointDetail  id => ' + item['id'])

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
                logger.error('明細に紐づくキャストが取得出来ません')

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
                    remarks=data['remarks'],
                )
            )

        logger.debug('★★★★★★最終局面★★★★★★')

        if len(sales_service_detail_list) > 0:
            SalesServiceDetail.objects.bulk_create(sales_service_detail_list)
        if len(sales_appoint_detail_list) > 0:
            SalesAppointDetail.objects.bulk_create(sales_appoint_detail_list)
        if len(sales_detail_list) > 0:
            SalesDetail.objects.bulk_create(sales_detail_list)

        return Response(SalesSerializer(header).data, status=status.HTTP_200_OK)


    @action(methods=['get'], detail=False)
    def get_day_sales_analytics(self, request):
        """
        指定した日から~間の売上を取得（日単位）
            => target_date=2022/6/18, range=3
                => 2022/6/18 (2022/6/18 20:30 ~ 2022/6/19:7:00)
                => 2022/6/19 (2022/6/19 20:30 ~ 2022/6/20:7:00)
                => 2022/6/20 (2022/6/20 20:30 ~ 2022/6/21:7:00)

        全期間は死ぬからNG, 最高1年くらい?かな
        """

        target_date_str = request.query_params['target_date'].split('-')
        target_date_year = int(target_date_str[0])
        target_date_hour = int(target_date_str[1])
        target_date_minute = int(target_date_str[2])

        # このrangeは繰り返しのcnt
        r = int(request.query_params['range'])

        res = []

        start_time = datetime(
            target_date_year,
            target_date_hour,
            target_date_minute,
            OPEN_HOUR,
            OPEN_MINUTE,
        ).astimezone(timezone('Asia/Tokyo'))

        for i in range(1, r+1):

            end_date = start_time + timedelta(days=1)
            end_time = datetime(
                end_date.year,
                end_date.month,
                end_date.day,
                CLOSE_HOUR,
                CLOSE_MINUTE,
            ).astimezone(timezone('Asia/Tokyo'))

            data = SalesHeader.objects.filter(
                visit_time__range=[
                    start_time,
                    end_time,
                ],
                leave_time__range=[
                    start_time,
                    end_time,
                ]).aggregate(total=models.Sum('total_tax_sales'))

            res.append({
                'date': start_time.strftime('%Y-%m-%d'),
                'total': data['total'] if data['total'] is not None else 0,
            })
            start_time = start_time + timedelta(days=1)

        return Response({
            'status': 'success',
            'data': res,
        })


    @action(methods=['get'], detail=False)
    def get_day_total_visitors_analytics(self, request):
        """
        指定した日から~間の売上を取得（日単位）
            => target_date=2022/6/18, range=3
                => 2022/6/18 (2022/6/18 20:30 ~ 2022/6/19:7:00)
                => 2022/6/19 (2022/6/19 20:30 ~ 2022/6/20:7:00)
                => 2022/6/20 (2022/6/20 20:30 ~ 2022/6/21:7:00)

        全期間は死ぬからNG, 最高1年くらい?かな
        """

        target_date_str = request.query_params['target_date'].split('-')
        target_date_year = int(target_date_str[0])
        target_date_hour = int(target_date_str[1])
        target_date_minute = int(target_date_str[2])

        # このrangeは繰り返しのcnt
        r = int(request.query_params['range'])

        res = []

        start_time = datetime(
            target_date_year,
            target_date_hour,
            target_date_minute,
            OPEN_HOUR,
            OPEN_MINUTE,
        ).astimezone(timezone('Asia/Tokyo'))

        for i in range(1, r+1):

            end_date = start_time + timedelta(days=1)
            end_time = datetime(
                end_date.year,
                end_date.month,
                end_date.day,
                CLOSE_HOUR,
                CLOSE_MINUTE,
            ).astimezone(timezone('Asia/Tokyo'))

            data = SalesHeader.objects.filter(
                visit_time__range=[
                    start_time,
                    end_time,
                ],
                leave_time__range=[
                    start_time,
                    end_time,
                ]).aggregate(total=models.Count('customer'))

            res.append({
                'date': start_time.strftime('%Y-%m-%d'),
                'total': data['total'] if data['total'] is not None else 0,
            })
            start_time = start_time + timedelta(days=1)

        return Response({
            'status': 'success',
            'data': res,
        })


    @action(methods=['get'], detail=False)
    def get_customer_day_sales_analytics(self, request):
        """
        指定した日の顧客ごとの売上を取得
        ・target_date
            => 2022/6/18 ・・・ 2022/6/18 20:30 ~ 2022/6/19 07:00
            => 2021/12/31 ・・・ 2021/12/31 20:30 ~ 2022/1/1 07:00
        """

        # logger.debug('★')
        # logger.debug(request.query_params)

        target_date_str = request.query_params['target_date'].split('-')
        target_date_year = int(target_date_str[0])
        target_date_hour = int(target_date_str[1])
        target_date_minute = int(target_date_str[2])

        range = int(request.query_params['range'])

        start_time = datetime(
            target_date_year,
            target_date_hour,
            target_date_minute,
            OPEN_HOUR,
            OPEN_MINUTE,
        ).astimezone(timezone('Asia/Tokyo'))
        end_date = start_time + timedelta(days=range)
        end_time = datetime(
            end_date.year,
            end_date.month,
            end_date.day,
            CLOSE_HOUR,
            CLOSE_MINUTE,
        ).astimezone(timezone('Asia/Tokyo'))

        data = SalesHeader.objects.filter(
            visit_time__range=[
                start_time,
                end_time,
            ],
            leave_time__range=[
                start_time,
                end_time,
            ]).values(
                'customer'
            ).annotate(
                total=models.Sum('total_tax_sales')
            ).order_by('-total')

        serializer = CustomerSalesSerializer(data, many=True)

        return Response({
            'status': 'success',
            'target_date': start_time.strftime('%Y-%m-%d'),
            'data': serializer.data,
        })

    # @action(methods=['get'], detail=False)
    # def get_customer_day_total_sales_analytics(self, request):
    #     """
    #     指定した日から~間の顧客毎の売上総計15件を取得
    #         => target_date=2022/6/18, range=3
    #             => 2022/6/18 (2022/6/18 20:30 ~ 2022/6/21:7:00)
    #                 の顧客の売上の上位15件
    #     全期間は死ぬからNG, 最高1年くらい?かな
    #     """
    #     target_date_str = request.query_params['target_date'].split('-')
    #     target_date_year = int(target_date_str[0])
    #     target_date_hour = int(target_date_str[1])
    #     target_date_minute = int(target_date_str[2])
    #
    #     range = int(request.query_params['range'])
    #
    #     start_time = datetime(
    #         target_date_year,
    #         target_date_hour,
    #         target_date_minute,
    #         OPEN_HOUR,
    #         OPEN_MINUTE,
    #     ).astimezone(timezone('Asia/Tokyo'))
    #     end_date = start_time + timedelta(days=range)
    #     end_time = datetime(
    #         end_date.year,
    #         end_date.month,
    #         end_date.day,
    #         CLOSE_HOUR,
    #         CLOSE_MINUTE,
    #     ).astimezone(timezone('Asia/Tokyo'))
    #
    #     data = SalesHeader.objects.filter(
    #         visit_time__range=[
    #             start_time,
    #             end_time,
    #         ],
    #         leave_time__range=[
    #             start_time,
    #             end_time,
    #         ]).values(
    #             'customer'
    #         ).annotate(
    #             total=models.Sum('total_tax_sales'),
    #         ).order_by('-total')[:15]
    #
    #     serializer = CustomerSalesSerializer(data, many=True)
    #
    #     return Response({
    #         'status': 'success',
    #         'target_date': start_time.strftime('%Y-%m-%d'),
    #         'data': serializer.data,
    #     })



    @action(methods=['get'], detail=False)
    def get_total_sales_analytics(self, request):
        """
        指定した日の売上の総計を取得
        ・target_date
            => 2022/6/18 ・・・ 2022/6/18 20:30 ~ 2022/6/19 07:00
            => 2021/12/31 ・・・ 2021/12/31 20:30 ~ 2022/1/1 07:00
        ・range => これがある場合、target_dateからrange(日)分取得する
            => target_date=2022/06/18, range=3 => 2022/06/18 20:30 ~ 2022/06/21 09:00

        ・日付指定なしならば全期間
        """

        if 'target_date' in request.query_params:
            # logger.debug(request.query_params['target_date'] + 'の売上総計を取得します。')
            target_date_str = request.query_params['target_date'].split('-')
            target_date_year = int(target_date_str[0])
            target_date_hour = int(target_date_str[1])
            target_date_minute = int(target_date_str[2])
            result_target_date = target_date_str

            range = int(request.query_params['range'])

            start_time = datetime(
                target_date_year,
                target_date_hour,
                target_date_minute,
                OPEN_HOUR,
                OPEN_MINUTE,
            ).astimezone(timezone('Asia/Tokyo'))

            end_date = start_time + timedelta(days=range)
            end_time = datetime(
                end_date.year,
                end_date.month,
                end_date.day,
                CLOSE_HOUR,
                CLOSE_MINUTE,
            ).astimezone(timezone('Asia/Tokyo'))

            data = SalesHeader.objects.filter(
                visit_time__range=[
                    start_time,
                    end_time,
                ],
                leave_time__range=[
                    start_time,
                    end_time,
                ]).aggregate(
                    total_price=models.Sum('total_tax_sales'),
                )
        else:
            # logger.debug('全期間の売上総計を取得します')
            data = SalesHeader.objects.aggregate(
                total_price=models.Sum('total_tax_sales'),
            )

        return Response({
            'status': 'success',
            'data': data,
        })

    @action(methods=['get'], detail=False)
    def get_total_visitors_analytics(self, request):
        """
        指定した日の来店数を取得（団体単位）
        ・target_date
            => 2022/6/18 ・・・ 2022/6/18 20:30 ~ 2022/6/19 07:00
            => 2021/12/31 ・・・ 2021/12/31 20:30 ~ 2022/1/1 07:00

            日付指定なしならば全期間
        """
        result_target_date = '全期間'

        if 'target_date' in request.query_params:
            # logger.debug(request.query_params['target_date'] + 'の来店数を取得します。')
            target_date_str = request.query_params['target_date'].split('-')
            target_date_year = int(target_date_str[0])
            target_date_hour = int(target_date_str[1])
            target_date_minute = int(target_date_str[2])
            result_target_date = target_date_str

            range = int(request.query_params['range'])

            start_time = datetime(
                target_date_year,
                target_date_hour,
                target_date_minute,
                OPEN_HOUR,
                OPEN_MINUTE,
            ).astimezone(timezone('Asia/Tokyo'))
            end_date = start_time + timedelta(days=range)
            end_time = datetime(
                end_date.year,
                end_date.month,
                end_date.day,
                CLOSE_HOUR,
                CLOSE_MINUTE,
            ).astimezone(timezone('Asia/Tokyo'))

            logger.debug('open : ' + start_time.strftime('%Y-%m-%d %H:%M'))
            logger.debug('end : ' + end_time.strftime('%Y-%m-%d %H:%M'))

            data = SalesHeader.objects.filter(
                visit_time__range=[
                    start_time,
                    end_time,
                ],
                leave_time__range=[
                    start_time,
                    end_time,
                ]).annotate(
                    models.Count('customer')
                ).values('customer').count()
        else:
            # logger.debug('全期間の来店数を取得します')
            data = SalesHeader.objects.values(
                'customer'
            ).annotate(
                models.Count('customer')
            ).values('customer').count()



        return Response({
            'status': 'success',
            'target_date': '-'.join(result_target_date),
            'data': data
        })

    @action(methods=['get'], detail=False)
    def get_basic_plan_type_ratio_analytics(self, request):
        """
        指定した日の基本料金比率
        ・target_date
            => 2022/6/18 ・・・ 2022/6/18 20:30 ~ 2022/6/19 07:00
            => 2021/12/31 ・・・ 2021/12/31 20:30 ~ 2022/1/1 07:00

            日付指定なしならば全期間
        """

        result_target_date = '全期間'

        if 'target_date' in request.query_params:
            # logger.debug(request.query_params['target_date'] + 'の基本料金比率を取得します。')
            target_date_str = request.query_params['target_date'].split('-')
            target_date_year = int(target_date_str[0])
            target_date_hour = int(target_date_str[1])
            target_date_minute = int(target_date_str[2])
            result_target_date = target_date_str

            range = int(request.query_params['range'])

            start_time = datetime(
                target_date_year,
                target_date_hour,
                target_date_minute,
                OPEN_HOUR,
                OPEN_MINUTE,
            ).astimezone(timezone('Asia/Tokyo'))
            end_date = start_time + timedelta(days=range)
            end_time = datetime(
                end_date.year,
                end_date.month,
                end_date.day,
                CLOSE_HOUR,
                CLOSE_MINUTE,
            ).astimezone(timezone('Asia/Tokyo'))

            logger.debug('open : ' + start_time.strftime('%Y-%m-%d %H:%M'))
            logger.debug('end : ' + end_time.strftime('%Y-%m-%d %H:%M'))

            data = SalesHeader.objects.filter(
                visit_time__range=[
                    start_time,
                    end_time,
                ],
                leave_time__range=[
                    start_time,
                    end_time,
                ]).values(
                    'basic_plan_type'
                ).annotate(
                    total=models.Count('basic_plan_type')
                )
        else:
            # logger.debug('全期間の基本料金比率を取得します')
            data = SalesHeader.objects.values(
                    'basic_plan_type'
                ).annotate(
                    total=models.Count('basic_plan_type')
                )

        # if len(data) == 0:
        #     data = [{'basic_plan_type':0, 'total': 0}, {'basic_plan_type':0, 'total': 0}]
        # if len(data) == 1:
        #     type = 0
        #     if data[0]['basic_plan_type'] == 0:
        #         type = 1
        #     data.({'basic_plan_type': type, 'total': 0})

        # 一旦0件でも1件も変える可能性があるやつで・・querysetに突っ込み方が分からん
        # 取得方法考えるか、突っ込み方考える
        return Response({
            'status': 'success',
            'target_date': '-'.join(result_target_date),
            'data': data
        })

    @action(methods=['get'], detail=False)
    def get_appoint_ratio_analytics(self, request):
        """
        指定した日の指名比率
        ・target_date
            => 2022/6/18 ・・・ 2022/6/18 20:30 ~ 2022/6/19 07:00
            => 2021/12/31 ・・・ 2021/12/31 20:30 ~ 2022/1/1 07:00

            日付指定なしならば全期間
        """

        result_target_date = '全期間'

        if 'target_date' in request.query_params:
            # logger.debug(request.query_params['target_date'] + 'の指名比率を取得します。')
            target_date_str = request.query_params['target_date'].split('-')
            target_date_year = int(target_date_str[0])
            target_date_hour = int(target_date_str[1])
            target_date_minute = int(target_date_str[2])
            result_target_date = target_date_str

            range = int(request.query_params['range'])

            start_time = datetime(
                target_date_year,
                target_date_hour,
                target_date_minute,
                OPEN_HOUR,
                OPEN_MINUTE,
            ).astimezone(timezone('Asia/Tokyo'))
            end_date = start_time + timedelta(days=range)
            end_time = datetime(
                end_date.year,
                end_date.month,
                end_date.day,
                CLOSE_HOUR,
                CLOSE_MINUTE,
            ).astimezone(timezone('Asia/Tokyo'))

            logger.debug('open : ' + start_time.strftime('%Y-%m-%d %H:%M'))
            logger.debug('end : ' + end_time.strftime('%Y-%m-%d %H:%M'))

            data = SalesHeader.objects.filter(
                visit_time__range=[
                    start_time,
                    end_time,
                ],
                leave_time__range=[
                    start_time,
                    end_time,
                ]).values(
                    'appoint'
                ).annotate(
                    total=models.Count('appoint')
                )
        else:
            # logger.debug('全期間の指名比率を取得します')
            data = SalesHeader.objects.values(
                    'appoint'
                ).annotate(
                    total=models.Count('appoint')
                )

        # if len(data) == 0:
        #     data = [{'basic_plan_type':0, 'total': 0}, {'basic_plan_type':0, 'total': 0}]
        # if len(data) == 1:
        #     type = 0
        #     if data[0]['basic_plan_type'] == 0:
        #         type = 1
        #     data.({'basic_plan_type': type, 'total': 0})

        # 一旦0件でも1件も変える可能性があるやつで・・querysetに突っ込み方が分からん
        # 取得方法考えるか、突っ込み方考える
        return Response({
            'status': 'success',
            'target_date': '-'.join(result_target_date),
            'data': data
        })

    @action(methods=['get'], detail=False)
    def get_customer_day_stay_hour_analytics(self, request):
        """
        顧客ごとの滞在時間 => その日で絞るだけ？・・・それだけだったらいらんかも。将来的になくすか検討
        """
        target_date_str = request.query_params['target_date'].split('-')
        target_date_year = int(target_date_str[0])
        target_date_hour = int(target_date_str[1])
        target_date_minute = int(target_date_str[2])

        start_time = datetime(
            target_date_year,
            target_date_hour,
            target_date_minute,
            OPEN_HOUR,
            OPEN_MINUTE,
        ).astimezone(timezone('Asia/Tokyo'))
        end_date = start_time + timedelta(days=1)
        end_time = datetime(
            end_date.year,
            end_date.month,
            end_date.day,
            CLOSE_HOUR,
            CLOSE_MINUTE,
        ).astimezone(timezone('Asia/Tokyo'))

        data = SalesHeader.objects.filter(
            visit_time__range=[
                start_time,
                end_time,
            ],
            leave_time__range=[
                start_time,
                end_time,
            ])

        # logger.debug(data)

        return Response({
            'status': 'success',
            'target_date': start_time.strftime('%Y-%m-%d'),
            # 'data': serializer.data,
            'data': SalesSerializer(
                data,
                many=True,
                fields=['id', 'customer', 'visit_time', 'leave_time']
            ).data,
        })


    @action(methods=['get'], detail=False)
    def get_product_day_sales_analytics(self, request):
        """
        指定した日の商品ごとの売上を取得
        ・target_date
            => 2022/6/18 ・・・ 2022/6/18 20:30 ~ 2022/6/19 07:00
            => 2021/12/31 ・・・ 2021/12/31 20:30 ~ 2022/1/1 07:00
        """

        target_date_str = request.query_params['target_date'].split('-')
        target_date_year = int(target_date_str[0])
        target_date_hour = int(target_date_str[1])
        target_date_minute = int(target_date_str[2])

        range = int(request.query_params['range'])

        start_time = datetime(
            target_date_year,
            target_date_hour,
            target_date_minute,
            OPEN_HOUR,
            OPEN_MINUTE,
        ).astimezone(timezone('Asia/Tokyo'))
        end_date = start_time + timedelta(days=range)
        end_time = datetime(
            end_date.year,
            end_date.month,
            end_date.day,
            CLOSE_HOUR,
            CLOSE_MINUTE,
        ).astimezone(timezone('Asia/Tokyo'))

        data = SalesHeader.objects.filter(
            visit_time__range=[
                start_time,
                end_time,
            ],
            leave_time__range=[
                start_time,
                end_time,
            ],
            sales_detail__isnull=False
            ).values(
                'sales_detail__product',
            ).annotate(
                total=models.Sum('sales_detail__total_tax_price'),
                total_cnt=models.Count('sales_detail__product')
            ).order_by('-total')[:20]

        serializer = ProductSalesSerializer(data, many=True)

        return Response({
            'status': 'success',
            'target_date': start_time.strftime('%Y-%m-%d'),
            'data': serializer.data,
        })


class BookingViewSet(BaseModelViewSet):
    """
    """
    permission_classes = (permissions.IsAuthenticated,)
    queryset = BookingManagement.objects.all()
    serializer_class = BookingSerializer

    # def list(self, request):
    #     queryset =


class AttendanceViewSet(BaseModelViewSet):
    """
    """
    permission_classes = (permissions.IsAuthenticated,)
    queryset = AttendanceManagement.objects.all()
    serializer_class = AttendanceSerializer


class TimeViewSet(viewsets.ViewSet):

    permission_classes = (permissions.IsAuthenticated,)
    queryset = MCustomer.objects.all()
    serializer_class = CustomerSerializer

    @action(methods=['get'], detail=False)
    def get_current_time(self, request):
        now = datetime.now().astimezone(timezone('Asia/Tokyo'))
        data = now.strftime('%Y-%m-%d %H:%M')
        return Response({
            'status': 'success',
            'data': data,
        })
