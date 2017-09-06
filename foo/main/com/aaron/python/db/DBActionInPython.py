"""
Python中的数据库操作

"""

import pymysql

url = "jdbc:mysql://192.168.1.133:3306/hotelsupplier?useUnicode=true&characterEncoding=utf8"

username = "hotel"

password = "hot4el"
connection = pymysql.connect(host="192.168.1.133", user=username, password=password,
                             port=3306, charset="utf8",
                             database="hotelsupplier")

cursor = connection.cursor()

cursor.execute("select * from hotelsupplier.haoqiao_hotel")

for row in cursor.fetchmany(20):
    print(row)
