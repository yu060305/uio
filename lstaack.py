'''
lstack.py  栈的链式结构
重点代码
'''
'''
思路：
1.源于节点存储数据,建立节点关联
2.封装方法　入栈　出栈　栈空　栈顶元素
3.链表的开头作为栈顶（不需要每次遍历）
'''
# 创建节点类
class Node:
    def __init__(self, val,next = None):
        self.val = val#有用的数据
        self.next = next#节点关系
class Lstack:
    def __init__(self):
        #标记栈顶位置
        self._top = None

if __name__ == '__main__':
    pass