import redis

r = redis.StrictRedis(host='127.0.0.1',port=6379,password='12345',decode_responses=True)

for x in range(3):
    r.publish('email','xxx@qq.com')



