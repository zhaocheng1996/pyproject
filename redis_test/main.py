import redis

# 192.168.1.15
#r = redis.Redis(host='127.0.0.1',post=6379,decode_responses=True,password='12345',db=0)
r = redis.StrictRedis(host='127.0.0.1',port=6379,password='12345',decode_responses=True)
# 操作字符串
r.set('username','zc1')

r.delete('username')
print(r.get('username'))#None

#列表操作
r.lpush('language','java')#加入列表中
r.lpush('language','python')
r.lpush('language','php')

# 集合操作
r.sadd('team','li')
r.sadd('team','huang')
r.sadd('team','zhang')
print(r.smembers('team'))#{'zhang', 'huang', 'li'}

# 哈希操作
r.hset('website','baidu','www,baidu.com')
r.hset('website','geogle','www,geogle.com')
print(r.hgetall('website'))
#{'baidu': 'www,baidu.com', 'geogle': 'www,geogle.com'}

# 事务
pip = r.pipeline()
pip.set('username','zc2')
pip.set('password','123')
print(r.get('username'))#None
print('+'*30)
# 写到这里执行后都不存到里面去
pip.execute()#这行后才会把前面所有的pip存入数据库中
print(r.get('username'))#zc2

#发布邮件功能
#异步发送邮件的功能
ps = r.pubsub()# 监听启动
ps.subscribe('email')
while True:
    for item in ps.listen():
        if item['type'] == 'message':
            data = item['data']
            print(data)















