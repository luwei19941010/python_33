#-*-coding:utf-8-*-
# Author:Lu Wei

from multiprocessing import Process
import time

def son1():
    while True:
        print('son1 alive')
        time.sleep(0.5)

if __name__=='__main__':
    p=Process(target=son1)
    p.start()

    print(1123)
    print(p.is_alive())
    time.sleep(2)
    p.terminate()
    print(p.is_alive())
    time.sleep(2)
    print(p.is_alive())
