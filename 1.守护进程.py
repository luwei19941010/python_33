#-*-coding:utf-8-*-
# Author:Lu Wei

from multiprocessing import Process
import time

def son1():
    while True:
        print('son1 alive')
        time.sleep(0.5)

def son2():
    for i in range(5):
        print('son2222')
        time.sleep(1)

if __name__=='__main__':
    p=Process(target=son1)
    p.daemon=True           #当主进程代码执行完毕时，回收守护进程资源，注意是主进程代码
    p.start()
    p2=Process(target=son2)
    p2.start()
    time.sleep(2)           #当所有的子进程执行完毕时，回收子进程资源，再进行主进程关闭