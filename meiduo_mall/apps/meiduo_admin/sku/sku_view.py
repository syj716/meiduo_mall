from datetime import date
from goods.models import SKU
from meiduo_admin.my_pagination import UserPageNum
from rest_framework.viewsets import ModelViewSet

from .sku_serializer import SkuSerializer, CategoryVisitCountSerializer, SPUSpecificationSerializer
from rest_framework.generics import ListAPIView
from goods.models import CategoryVisitCount

from goods.models import SPUSpecification


class GoodsDayView(ListAPIView):
    serializer_class =CategoryVisitCountSerializer
    queryset = CategoryVisitCount.objects.filter(date=date.today()).all()
class SkuView(ListAPIView):
    serializer_class =SkuSerializer
    #queryset =SKU.objects.all()
    pagination_class = UserPageNum
    def get_queryset(self):
        keyword=self.request.query_params.get("keyword")
        if keyword is '' or keyword is None:
            return SKU.objects.all()
        else:
            return SKU.objects.filter(name__contains=keyword).all()

class GoodSpecsView(ListAPIView):
    pagination_class = UserPageNum
    serializer_class = SPUSpecificationSerializer
    def get_queryset(self):
        spu_id=self.request.query_params.get("spu_id")
        return SPUSpecification.objects.filter(spu_id=spu_id).all()