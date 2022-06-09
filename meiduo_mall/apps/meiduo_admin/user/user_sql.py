from django.db import connection
from django.http import HttpResponse
def selectUserTotalCount():
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT count(*) FROM tb_users")
        return cursor.fetchall()
    finally:
        cursor.close()
        connection.close()
def CountUserDayIncrement(data):
    try:
        cursor = connection.cursor()
        # sql="SELECT count(*) FROM tb_users where date_joined=%d"
        sql="SELECT count(*) FROM tb_users where date_joined={}".format(data)
        cursor.execute(sql)
        return cursor.fetchall()
    finally:
        cursor.close()
        connection.close()
def CountUserDayActive(data):
    try:
        cursor = connection.cursor()
        sql="SELECT count(*) FROM tb_users where last_login={}".format(data)
        cursor.execute(sql)
        return cursor.fetchall()
    finally:
        cursor.close()
        connection.close()
def CountUserDayOrders(data):
    try:
        cursor = connection.cursor()
        sql="SELECT count(*) FROM tb_users where orderinfo__create_time={}".format(data)
        cursor.execute(sql)
        return cursor.fetchall()
    finally:
        cursor.close()
        connection.close()