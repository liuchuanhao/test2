# -*- coding: utf-8 -*-



import pymysql
import redis

if __name__ == '__main__':
    pool = redis.ConnectionPool(host="127.0.0.1", port=6379, db=0)
    r = redis.Redis(connection_pool=pool)
    dbconn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="123456", database="redis_mysql")
    cur = dbconn.cursor()
    cur.execute("select * from tb_signin_rank")
    data = cur.fetchall()
    print(data)
    dbconn.close()

    db_cursor = dbconn.cursor()
    for i in range(1, 6):
        dbconn.ping()
        db_cursor.execute('UPDATE tb_signin_rank SET signin_num = signin_num + 1, signin_time = NOW(), gold_coin = gold_coin + (1 + RAND()*9) WHERE id = {}'.format(i))
        db_cursor.execute("commit")

    r.zincrby("tb_signin_rank:id:signin_num", id, 1)

    for id in range(1, 6):
        result = r.zscore('tb_signin_rank:id:signin_num', id)
        if not result:
            print("-从数据库读取用户签到次数")
            try:
                db_cursor = dbconn.cursor()
                db_cursor.execute('SELECT signin_num FROM tb_signin_rank WHERE id = %s', (id,))
                result = db_cursor.fetchone()[0]
                # 更新到缓存
                r.zadd('tb_signin_rank:id:signin_num', id, result)
            except Exception as e:
                print('执行数据库查询操作失败：%s' % e)
                db_cursor.close()
        else:
            print("-从缓存读取用户签到次数-----------")
            result = int(result)

        print('sigin_num of user[id=%s]: %s' % (id, result))

    result = r.zrevrange('tb_signin_rank:id:signin_num', 0, 10)
    print('签到排行榜：', result)


