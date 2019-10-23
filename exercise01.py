import pymysql
#链接数据库
db=pymysql.connect(host='localhost',
                   port=3306,
                   user='root',
                   password='123456',
                   database='stu',
                   charset='utf8')
#生成游标对象(操作数据库,执行sql语句)
cur=db.cursor()
# s=input("请输入姓别:")
#执行读操作(输入姓名查询信息)
# sql="select * from class_1 where name='%s';"%s
# cur.execute(sql)#执行语句
#查询性别为男,分数>85,在class_1中:
# score=float(input("请输入大于的分数:"))
# sql="select * from class_1 where sex='%s'and score>%s;"%(s,score)
sql="select * from class_1 where sex=%s and score>%s;"
cur.execute(sql,['m',85])#执行语句
#迭代cur获取查询
# for i in cur:
#     print(i)
#获取一个查询结果
# one_row=cur.fetchone()
# print(one_row)
#获取多个查询结果
# many_row=cur.fetchmany(4)
# print(many_row)
#获取所有查询结果
all_row=cur.fetchall()
print(all_row)
#关闭游标和数据库链接
cur.close()
db.close()