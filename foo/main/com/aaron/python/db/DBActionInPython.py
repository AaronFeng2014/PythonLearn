"""
Python中的数据库操作
    操作数据库的步骤是固定的

    1. 获取数据库连接
    2. 从互数据库连接中获取游标
    3. 利用游标执行数据库脚本
    4. 从游标中获取数据

"""
# 引入mysql模块
import pymysql

url = "jdbc:mysql://192.168.1.133:3306/hotelsupplier?useUnicode=true&characterEncoding=utf8"

# 根据配置链接数据库没获取connection
connection = pymysql.connect(host="192.168.1.133",
                             user="hotel",
                             password="hot4el",
                             port=3306,
                             charset="utf8",
                             use_unicode=True,
                             database="hotelsupplier")
# 从数据库连接中获取一个数据库游标
cursor = connection.cursor()

sql = "select * from hotelsupplier.haoqiao_hotel limit 10000,3"

# 利用游标执行数据库脚本
cursor.execute(sql)

# 执行脚本后，从游标中获取数据,获取的数据行是元组结构
data = cursor.fetchall()
for row in data:
    print(row)
    for cell in row:
        print(cell)

# 执行建表语句
# cursor.execute("create table test_table(name varchar(200) not NULL)")
