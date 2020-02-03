#-*-coding:utf-8-*-
# Author:Lu Wei
from multiprocessing import  Process
import time

# class MYserver1(Process):
#     def __init__(self,a,b):
#         super().__init__()
#         self.x=a
#         self.y=b
#
#     def run(self):
#         while True:
#             time.sleep(1)
#             print('MYserver1')
#
# class MYserver2(Process):
#     def run(self):
#         for i in range(5):
#             time.sleep(1)
#             print('MYserver2222')
#
# if __name__=='__main__':
#     a=time.time()
#     cp1=MYserver1(1,2)
#     cp1.daemon=True
#     cp1.start()
#     time.sleep(2)
#     cp2=MYserver2()
#     cp2.start()
#     time.sleep(4)
#     c=time.time()-a
#     print(c)
#
#






class MYSERVER3(Process):
    # def __init__(self):
    #     self.a=a
    #     self.b=b
    #     super().__init__()
    def run(self):
        while True:
            print(1)
            time.sleep(1)
            print('MY3333')


if __name__=='__main__':
    p=MYSERVER3()      #实例化一个进程对象
    #p.daemon = True

   #  print(p.is_alive())
    p.start()
    p.terminate()
    time.sleep(0.01)
    print(p.is_alive())#开启
















