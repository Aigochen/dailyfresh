# -*- coding:utf-8 -*-
import MySQLdb
# connection 用于数据库连接，获取数据库对象，cursor，数据库交互对象，exception数据库异常类
# 流程：创建connection,创建数据库连接对象，然后调用cursor方法，返回cursor对象，对数据库进行操作，cursor调用##方法，执行命令，获取数据处理出数据，然后关闭cursor，关闭cnnection（否则占用资源）,结束。
# connection对象的方法：cursor()：使用该链接并返回游标，commit()提交当前事务,rollback()回滚当前事务，##close()关闭连接 。
# 游标对象，由于执行查询和获取结果。excute(),执行数据库查询和命令，将数据库语句送到数据库执行，数据库将对象##返回客户端缓冲池。
# fetchone()去的结果集的下一行。##fetchmany(size)获取结果集的下几行，fetchall()：获取结果##集中的剩下所有行,rowcount()：
# 最近一次execute返回数##据的行数或者影响的行数。close()：关闭是游标对象。##fetch*()方法，通过rownumber指针返回数据，比如开始时候，rownumber=0，调用fetchone，ruwnumber+1,返回第一条数据。

# 建立数据库连接
db = MySQLdb.connect(
    # mysql服务器地址
    host="127.0.0.1",
    # mysql服务器端口号
    port=3306,
    # 用户名
    user="root",
    # 密码
    passwd="",
    # 数据库名
    db="test",
    # 连接编码
    charset='utf8'
)
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# print db
# print cursor
# 使用execute方法执行SQL语句
cursor.execute("SELECT VERSION()")

# 使用fetch方法进行遍历结果，总共有三条数据
# data=cursor.fetchone() # 将第一条结果放入data中
# data=cursor.fetchmany() # 将多个结果放入data中 还有一个：fetchall()，将所有的的
data = cursor.fetchone()
# 打印数据库版本
print ("Database version: %s" % data)
# 关闭数据库连接
db.close()
