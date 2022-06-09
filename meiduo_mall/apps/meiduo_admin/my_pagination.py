from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class UserPageNum(PageNumberPagination):
    page_size = 5  # 后端指定每页显示数量
    page_size_query_param = 'pagesize'
    max_page_size = 10

    # 重写响应值的方法
    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,  # 总数量
            'lists': data,  # 用户数据
            'page': self.page.number,  # 当前页数
            'pages': self.page.paginator.num_pages,  # 总页数
            'pagesize': self.page_size  # 后端指定的页容量

        })