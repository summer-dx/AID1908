"""
   创建数据库 dict 使用utf8编码
   创建表 words分为三个字段
   id（自增）       word      mean
   将dict.txt 中的所有单词存入到该数据表当中

"""


import pymysql
import re

# 连接数据库
db = pymysql.connect(host = "localhost",
                     port = 3306,
                     user = "root",
                     password = "123456",
                     database = "dict",
                     charset = "utf8")

# 生成游标对象（操作数据库，执行sql语句）
cur = db.cursor()

# 执行各种对数据库的写操作
fr = open("dict.txt","r")
args_list = []

for line in fr:
     #     获取单词和解释
    tup = re.findall(r"(\S+)\s+(.*)",line)[0]
    args_list.append(tup)

fr.close()

try:
    sql = "insert into words (word,mean) values(%s,%s);"
    cur.executemany(sql,args_list)
    db.commit()

except Exception as e:
    db.rollback()  # 事务回滚
    print(e)

# 关闭游标 和数据连接
cur.close()
db.close()



def fun():
   print('哈哈哈哈')
