
from goods.models import SKU
from goods.models import CategoryVisitCount
from rest_framework import serializers

from goods.models import SPU, GoodsCategory

from goods.models import SPUSpecification, SpecificationOption


class CategoryVisitCountSerializer(serializers.ModelSerializer):
    # 1,重写category, 目的,在序列化的时候,将category数据,显示成汉字形式
    # category = serializers.StringRelatedField(read_only=True)
    category = serializers.CharField(read_only=True)
    class Meta:
        model = CategoryVisitCount
        fields = ('count','category')


class SPUSerializer(serializers.ModelSerializer):
    class Meta:
        model = SPU
        fields = ('id','name')
class GoodsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = ('id','name')
class SkuSerializer(serializers.ModelSerializer):
    spu=SPUSerializer(read_only=True)
    category=GoodsCategorySerializer(read_only=True)
    class Meta:
        model = SKU
        fields = "__all__"
class SpecificationOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecificationOption
        fields = ("id","value")

class SPUSpecificationSerializer(serializers.ModelSerializer):
    options = SpecificationOptionSerializer(read_only=True, many=True)
    class Meta:
        model = SPUSpecification
        fields =  "__all__"
