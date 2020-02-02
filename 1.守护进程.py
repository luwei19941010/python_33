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
    p.daemon=True
    p.start()
    p2=Process(target=son2)
    p2.start()
    time.sleep(2)