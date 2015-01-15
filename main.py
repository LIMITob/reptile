#!/usr/bin/env python
# coding=utf-8
# jetson@2014-12-19 21:19:23

import time,os
import threading
import getUrl
import reptile


cnt = 0
url = getUrl.getUrl('http://tieba.baidu.com/f/good?kw=%E6%B0%B8%E5%A4%9C%E5%90%9B%E7%8E%8B&ie=utf-8&cid=4&pn=')
lock = threading.Lock()
def downLoad(no,a):
    '''
    每个线程处理n个页面
    '''
    lock.acquire()
    if (a+1)*no > len(url):
        url_part = url[a*no:]
    else:
        url_part = url[a*no:(a+1)*no]
    lock.release()

    for i in url_part:
        reptile.grap1page(i)
        

def assignTask():
    thread_num = len(url)/20 + 1
    print '%d threads will start'%thread_num
    threads = []
    for i in range(thread_num):
        a = threading.Thread(target=downLoad,args=(20,i))
        threads.append(a)
    for j in threads:
        j.start()
    for k in threads:
        k.join()


if __name__ == '__main__':  
    assignTask()  
