#-*-coding:utf-8-*-
# Author:Lu Wei
from multiprocessing import Process,Queue

# n=1000
# def func():
#     global n
#     n-=1
#     print(n)
#
# if __name__=='__main__':
#     p_l=[]
#     for i in range(10):
#         p=Process(target=func)
#         p.start()
#         p_l.append(p)
#     for i in p_l:i.join()
#     print('___>>>',n)

def func(exp,q):
    ret=eval(exp)
    q.put({ret,1,2})
    q.put(2*ret)
    q.put(3*ret)
    q.put(4*ret)

##Queue 先进先出
if __name__=='__main__':
    q=Queue()
    Process(    target = func, args = ('1+2+3', q)).start()
    print(q.get())
