'''
链式队列
'''
'''
思路分析：
1.基于链表构建模型
2.链表的头作为队头，尾作为队尾
3.定义两个标记　标记队头和队尾
4.头和尾代表通用一个无用节点时队列为空
'''
#自定义异常
class QueueError(Exception):#继承父类
    pass

# 创建节点类
class Node:
    def __init__(self, val,next = None):
        self.val = val#有用的数据
        self.next = next#节点关系
# 队列操作
class LQueue:
    def __init__(self):#数据
        # front队头      rear队尾
        self.front = self.rear = Node(None)
        #添加的时候，头动尾不动
#判断栈内是否为空
    def is_empty(self):
        return self.front ==self.rear#如果头和尾相等返回
# 链式入队
    def enqueue(self,val):
       self.rear.next = Node(val)#将新节点等于rear.next的下一个(连上了），
       self.rear = self.rear.next#rear向后走一位

#链式出队
    def dequeue(self):
        if self.is_empty():#如果列表内为空，报错
            raise QueueError('Quue is empty')
        # frontd　是指向队头节点的前一个
        self.frontd = self.frontd.next
        return self.frontd.val
    #实际上frontd.指向的那个数据还在链表内，只不过不发生作用，还是有值的


if __name__ == '__main__':
    lq = LQueue()
    lq.enqueue(10)
    lq.enqueue(20)
    lq.enqueue(30)
    while not lq.is_empty():
        print(lq.dequeue())