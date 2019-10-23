import pymysql
import re
#链接数据库
db=pymysql.connect(host='localhost',
                                                                   port=3306,
                   user='root',
                   password='123456',
                   database='test',
                   charset='utf8')
cur=db.cursor()
with open('','rb') as f:
    data=f.read()
try:
    sql='insert into image values(1,%s,%s);'
    cur.execute(sql,['',data])
    db.commit()
except:
    db.rollback()