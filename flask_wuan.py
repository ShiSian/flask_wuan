# _*_ coding:utf-8 _*_
from flask import Flask
import pymysql
import json


# 解决编码问题
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


app = Flask(__name__)


@app.route('/')
def index():
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "mysql123", "wuan_mission" )
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # 创建并执行SQL语句
    sql = """SELECT * FROM comment """
    try:
        cursor.execute(sql)
        comment = cursor.fetchall()
    except Exception as e:
        print(e)
        db.rollback()
    # 关闭数据库连接
    db.close()
    # 输出评论
    result = comment[0][1]
    json_str = json.dumps(result)
    f = open('D:\\0000\\json_file.txt', 'w')
    f.write(json_str)
    f.close()
    return result


if __name__ == '__main__':
    app.run()
