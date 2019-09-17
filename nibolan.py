'''
自己编写一个逆波兰表达式程序
'''
from sstack import *
# 先导入模块
# 创建一个栈
# 循环输入类表达式

st = SStack()
while True:
    exp = input()
    tmp = exp.strip(' ')#用空格切割成列表
    for i in tmp:# 遍历这个列表
        if i =='+':
            y = st.pop()
            x = st.pop()
            st.push(x+y)

        elif i == '-':
            y = st.pop()
            x = st.pop()
            st.push(x - y)
        elif i == '*':
            y = st.pop()
            x = st.pop()
            st.push(x * y)
        elif i == '/':
            y = st.pop()
            x = st.pop()
            st.push(x / y)
        elif i == 'p':
            print(st.pop())#查看栈顶元素
        else:
            st.push(int(i))
