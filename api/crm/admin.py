from django.contrib import admin

from .models import (
    mUser,
    MRank,
    MTax,
    MCustomer,
    MCast,
    MProduct,
    MSeat
)

from .sub_models import (
    CardManagement,
    BottleManagement,
    SalesHeader,
    SalesDetail,
    BookingManagement,
    AttendanceManagement,
)

admin.site.register(mUser)
admin.site.register(MRank)
admin.site.register(MTax)
admin.site.register(MCustomer)
admin.site.register(MCast)
admin.site.register(MProduct)
admin.site.register(MSeat)
admin.site.register(CardManagement)
admin.site.register(BottleManagement)
admin.site.register(SalesHeader)
admin.site.register(SalesDetail)
admin.site.register(BookingManagement)
admin.site.register(AttendanceManagement)
