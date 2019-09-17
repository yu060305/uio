'''
两个栈实现队列
'''
from sstack import *
class MyQueue:
    def __init__(self):
        self.en_srack = SStack()# 初始化入队栈
        self.de_srack = SStack()#初始化出对栈
    def is_empty(self):
        if self.en_srack.is_empty()and self.de_srack.is_empty():#当出入站为空
            return True
        else:
            return False
    def enqueue(self,val):
       while not self.de_srack.is_empty(): #
           self.en_srack.push(self.de_srack.pop())#先把出队栈内的数放入出队栈，然后在放入新的数
       self.en_srack.push(val)
    def dequeue(self):
        if self.is_empty():
            raise Exception('ERROR')#判断否为空
        while not self.en_srack.is_empty():  # 先判断入队的栈内是否为空
            self.de_srack.push(self.en_srack.pop())  # 先把出队栈内的数放入出队栈，然后在放入新的数
        return self.de_srack.pop()

q = MyQueue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
while not q.is_empty():#判断栈内是否为空
    print(q.dequeue())#打印出栈