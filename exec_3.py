'''
队列内容反转
'''
from squeue import *
#导入模块
from sstack import *
# 导入栈，用于中专数据
# 方法：
# 队入栈，栈出入队
sq = SQueue()
ls = SStack()#栈

# 出队入栈
while not sq.is_empty():#如果栈不为空
    ls.push(sq.denqueue())#将sq队列的值出队列并入ls入栈
# 出栈入队
while not ls.is_empty():#如果ls栈不为空，执行下面操作
    sq.enqueue(ls.pop())#将ls栈里面的值出栈到队列
while not sq.is_empty():#如果队列栈不为空
    print(sq.is_empty())#打印队列栈
