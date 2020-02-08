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
#
# def func(exp,q):
#     ret=eval(exp)
#     q.put({ret,1,2})
#     q.put(2*ret)
#     q.put(3*ret)
#     q.put(4*ret)
#
# ##Queue 先进先出
#
# if __name__=='__main__':
#     q = Queue()
#     Process(target = func, args = ('1+2+3', q)).start()
#     print(q.get())
#     print(q.get())
#     print(q.get())
#     print(q.get())
import queue
q=Queue(3)   # 设置队列长度
q.put(1)     # 放入数据
q.put(2)
q.put(3)
print(123)          #当队列为满的时候再向队列中放数据 队列会阻塞
try:
    q.put_nowait(4) # 当队列为满的时候再向队列中放数据 会报错并且会丢失数据
except queue.Full:
    pass
print(12345)

print(q.get())
print(q.get())
print(q.get())
try:
    print(q.get_nowait())   # 在队列为空的时候 直接报错
except queue.Empty:         #报错类型在queue模块中，所以要import queue
    pass
print(q.get())   # 在队列为空的时候会发生阻塞
print(q.get())   # 在队列为空的时候会发生阻塞
