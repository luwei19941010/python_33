#-*-coding:utf-8-*-
# Author:Lu Wei

from  multiprocessing import Process,Lock
import time,os
import json


def serach_tick(user):
    with open('aaa','r')  as f:
        dic=json.load(f)
        print('%s查询结果:%s张余票'%(user,dic['count']))

def buy_tick(user,lock):
    # lock.acquire()
    with lock:
        time.sleep(0.2)
        with open('aaa','r')  as f:
            dic=json.load(f)
            if dic['count']>0:
                print('%s买到票了'%(user))
                dic['count'] -= 1
            else:
                print('%s没买到票了' % (user))
            time.sleep(0.2)
            with open('aaa','w') as f:
                json.dump(dic,f)
    # lock.release()


def task(user,lock):
   serach_tick(user)
   # with lock:
   buy_tick(user,lock)


if __name__=='__main__':
    lock = Lock()
    for i in range(10):
        p=Process(target=task,args=('user%s'%i,lock))
        p.start()
#

"""

def search_ticket(user):
    with open('aaa') as f:
        dic = json.load(f)
        print('%s查询结果  : %s张余票'%(user,dic['count']))

def buy_ticket(user,lock):
    with lock:      # with lock和lock.acquire建议with lock
    # lock.acquire()   # 给这段代码加上一把锁,release解锁
        time.sleep(0.02)
        with open('aaa') as f:
            dic = json.load(f)
        if dic['count'] > 0:
            print('%s买到票了'%(user))
            dic['count'] -= 1
        else:
            print('%s没买到票' % (user))
        time.sleep(0.02)
        with open('aaa','w') as f:
            json.dump(dic,f)
    # lock.release()   # 给这段代码解锁

def task(user, lock):
    search_ticket(user)
    with lock:
        buy_ticket(user, lock)

if __name__ == '__main__':
    lock = Lock()
    for i in range(10):
        p = Process(target=task,args=('user%s'%i,lock))
        p.start()
"""