import redis

def conuter(video_id: int):
    result = client.get(video_id)
    if not result:
        client.set(video_id, 1)
        return 1
    else:
        count_number = client.incr(video_id)
        return count_number


if __name__ == '__main__':
    try:
      client = redis.Redis(host='192.168.56.50', password='myegoo3466')
    except Exception as e:
        print(e)

    print(conuter(1001))  # 返回 1
    print(conuter(1001))  # 返回 2
    print(conuter(1002))  # 返回 1
    print(conuter(1001))  # 返回 3
    print(conuter(1002))  # 返回 2