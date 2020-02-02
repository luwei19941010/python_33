#-*-coding:utf-8-*-
# Author:Lu Wei
from multiprocessing import  Process
import time

class MYserver1(Process):
    def __init__(self,a,b):
        super().__init__()
        self.x=a
        self.y=b

    def run(self):
        while True:
            time.sleep(1)
            print('MYserver1')

class MYserver2(Process):
    def run(self):
        for i in range(5):
            time.sleep(1)
            print('MYserver2222')

if __name__=='__main__':
    a=time.time()
    cp1=MYserver1(1,2)
    cp1.daemon=True
    cp1.start()
    time.sleep(2)
    cp2=MYserver2()
    cp2.start()
    time.sleep(4)
    c=time.time()-a
    print(c)