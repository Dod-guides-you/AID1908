import pymysql
import re
#链接数据库
db=pymysql.connect(host='localhost',
                   port=3306,
                   user='root',
                   password='123456',
                   database='dict',
                   charset='utf8')
cur=db.cursor()
arg_list=[]

f=open('dict.txt','r')
for line in f:
    tup=re.findall(r"(\S+)\s+(.*)",line)[0]
    # arg_list.append(tup)
    print(tup)
f.close()
sql = "insert into words (word,mean)values(%s,%s);"
try:
    cur.executemany(sql, arg_list)
    db.commit()#将操作结果立即提交
except:
    db.rollback()
cur.close()
db.close()