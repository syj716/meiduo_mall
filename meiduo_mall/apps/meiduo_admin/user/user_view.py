from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import User
from datetime import date, timedelta
from meiduo_admin.my_pagination import UserPageNum
from .user_serializer import UserSerializer,UserAddSerializer
from .user_sql import selectUserTotalCount, CountUserDayIncrement, CountUserDayActive, CountUserDayOrders

'''
# 1, 获取用户总数
class UserTotalCountView(APIView):

    #1, 设置管理员权限
    permission_classes = [IsAdminUser]

    def get(self,request):
        # 1, 查询用户总数
        count = User.objects.filter(is_staff=False).count()

        # 2, 返回响应
        return Response({
            "count":count
        })
'''
# 1, 获取用户总数
class UserTotalCountView(APIView):
   # permission_classes = [IsAdminUser]
    def get(self,request):
        count=selectUserTotalCount()
        # count=User.objects.filter(is_staff=False).count()
        return Response(
            {
                "count":count
            }
        )
# 2, 获取日增用户
class UserDayIncrementView(APIView):
   # permission_classes = [IsAdminUser]
    def get(self,request):
        count=CountUserDayIncrement(date.today())
        # count=User.objects.filter(date_joined__gte=date.today(),is_staff=False).count()
        return Response({
            "count": count
        })
'''
# 2, 获取日增用户
class UserDayIncrementView(APIView):

    #1, 设置管理员权限
    permission_classes = [IsAdminUser]

    def get(self,request):
        # 1, 查询用户日增数量, 注意点: date.today() 获取的不带时分秒
        count = User.objects.filter(date_joined__gte=date.today(),is_staff=False).count()

        # 2, 返回响应
        return Response({
            "count":count
        })
'''
# 3, 获取日活用户
class UserDayActiveView(APIView):
    def get(self,request):
        # 1, 查询用户日活数量
        count=CountUserDayActive(date.today())
        # 2, 返回响应
        return Response({
            "count":count
        })

# 4, 获取日下单用户
class UserDayOrdersView(APIView):
    def get(self,request):
        # 1, 查询用户日下单用户数量
        # count=CountUserDayOrders(date.today())
        count = User.objects.filter(orderinfo__create_time__gte=date.today() ,is_staff=False).count()
        # 2, 返回响应
        return Response({
            "count":count
        })
#获取月增加用户
class UserMonthCountView(APIView):
    def get(self,request):
        now_date = date.today()
        # 获取一个月前日期
        start_date = now_date - timedelta(29)
        date_list=[]
        for i in (1,31):
            current_date=start_date+timedelta(days=i)
            next_date=current_date+timedelta(days=i+1)
            count=User.objects.filter(date_joined__gte=current_date, date_joined__lt=next_date).count()
            date_list.append({
                'count':count,
                'date':current_date
            })
        return Response(date_list)
class UserView(ListCreateAPIView):
    pagination_class = UserPageNum
    def get_queryset(self):
        keyword=self.request.query_params.get('keyword')
        if keyword is '' or keyword is None:
            return User.objects.all()
        else:
            return User.objects.filter(username=keyword)
    def get_serializer_class(self):
        if self.request.method == "POST":
            return UserAddSerializer
        else:
            return UserSerializer
