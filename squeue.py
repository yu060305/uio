'''
顺序队列
'''
'''
思路分析：
1.基于列表完成数据的存储
2.通过封装一定的功能完成队列的基本行为
3.无论那边做队头或者是队尾　　都不是很完美（都会在内存中移动）

'''
#自定义异常
class QueueError(Exception):#继承父类
    pass

#队列操作
class SQueue:
    def __init__(self):#初始化
        self._elems = []#数据，定义一个新列表　 # 用来承载数据
# 判断队列是否为空
    def is_empty(self):#行为：
        return self._elems ==[]
# 入队
    def enqueue(self,val): #定义方法 直接添加元素
        self._elems.append(val)
#出队(如果一开始用户就直接删除出队，　假设当前是控列表，会报错，自己加个判断并自定义抛出异常)
    def denqueue(self):
        if not self._elems:#如果他是空列表,报错
            raise QueueError('Quue is empty')
        return self._elems.pop(0)#弹出第一个数据(删除第一个）并返回




if __name__ == '__main__':
    sq = SQueue()#创建类变量
    sq.enqueue(10)#进队
    sq.enqueue(20)#进队
    sq.enqueue(30)#进队
    while not sq.is_empty():#????
        print(sq.denqueue())#????


