from rest_framework import (
    permissions,
    viewsets,
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


class BaseModelViewSet(viewsets.ModelViewSet):
    """
    """


class CustomerViewSet(BaseModelViewSet):
    """
    """
    permission_classes = (permissions.AllowAny,)
    queryset = MCustomer.objects.all()
    serializer_class = CustomerSerializer


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
