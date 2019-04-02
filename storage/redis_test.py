import redis
conn = redis.Redis()
conn.hmset('test', {'count': 1, 'name': 'Fester Bestertester'})
print(conn.hgetall('test'))
conn.hsetnx('test', 'count', 3)
print(conn.hgetall('test'))

