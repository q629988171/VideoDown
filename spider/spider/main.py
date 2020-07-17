# !/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import os
import threading
import time
import json
from trd.mythread import myThread

# 创建双线程
def create_thread(res):
    thread = myThread(res['id'], res['title'], res['id'])
    thread.start()


def main():
    i = 1
    while True:
        print("收藏夹页数: %d" % i)
        url = 'https://api.bilibili.com/medialist/gateway/base/spaceDetail?media_id=88854277&pn=' + \
            str(i) + '&ps=20&keyword=&order=mtime&type=0&tid=0&jsonp=jsonp'
        html = requests.get(url)
        res = json.loads(html.text)
        try:
            len_video = len(res['data']['medias'])
            print("视频数量: %d" % len_video)
        except KeyError:
            print("视频数量: 0")
            break
        for id in range(0, len_video):
            create_thread(res['data']['medias'][id])
        time.sleep(1)
        i += 1


if __name__ == "__main__":
    main()
