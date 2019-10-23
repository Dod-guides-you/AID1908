import pymysql
#链接数据库
db=pymysql.connect(host='localhost',
                   port=3306,
                   user='root',
                   password='123456',
                   database='stu',
                   charset='utf8')
cur=db.cursor()
try:
    #执行增改等语句
    # sql="insert into class_1 (name,age,score)values('Dave',13,77);"
    exe=[]
    for i in range(3):
        name=input("Name:")
        age=int(input("Age:"))
        score=float(input("Score:"))
        exe.append((name,age,score))
    sql = "insert into class_1 (name,age,score)values(%s,%s,%s);"
    # cur.execute(sql,[name,age,score])
    cur.executemany(sql, exe)
    db.commit()#将操作结果立即提交
except Exception as e:
    db.rollback()
    print(e)
cur.close()
db.close()