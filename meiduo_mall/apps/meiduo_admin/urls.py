from django.conf.urls import url
from rest_framework import routers

from rest_framework_jwt.views import obtain_jwt_token

from .sku import sku_view
from .user import user_view

urlpatterns = [
    url(r'^authorizations/$',obtain_jwt_token),
    url(r'^statistical/total_count/$',user_view.UserTotalCountView.as_view()),
    url(r'^statistical/day_increment/$',user_view.UserDayIncrementView.as_view()),
    url(r'^statistical/day_active/$',user_view.UserDayActiveView.as_view()),
    url(r'^statistical/day_orders/$',user_view.UserDayOrdersView.as_view()),
    url(r'^statistical/month_increment/$',user_view.UserMonthCountView.as_view()),
    url(r'^statistical/goods_day_views/$',sku_view.GoodsDayView.as_view()),
    url(r'^users/$',user_view.UserView.as_view()),
    url(r'^skus/$',sku_view.SkuView.as_view()),
    url(r'^specsView/$',sku_view.GoodSpecsView.as_view()),
]
# router=routers.SimpleRouter()
# router.register(r'skus',sku_view.SkuView,base_name="skus")
# urlpatterns+=router.urls