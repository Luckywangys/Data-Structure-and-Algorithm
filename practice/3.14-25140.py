'''
描述
后序算术表达式可以通过栈来计算其值，做法就是从左到右扫描表达式，碰到操作数就入栈，碰到运算符，就取出栈顶的2个操作数做运算(先出栈的是第二个操作数，后出栈的是第一个)，并将运算结果压入栈中。最后栈里只剩下一个元素，就是表达式的值。
有一种算术表达式不妨叫做“队列表达式”，它的求值过程和后序表达式很像，只是将栈换成了队列：从左到右扫描表达式，碰到操作数就入队列，碰到运算符，就取出队头2个操作数做运算（先出队的是第2个操作数，后出队的是第1个），并将运算结果加入队列。最后队列里只剩下一个元素，就是表达式的值。
给定一个后序表达式，请转换成等价的队列表达式。例如，"3 4 + 6 5 * -"的等价队列表达式就是"5 6 4 3 * + -" 。
输入
第一行是正整数n(n<100)。接下来是n行，每行一个由字母构成的字符串，长度不超过100,表示一个后序表达式，其中小写字母是操作数，大写字母是运算符。运算符都是需要2个操作数的。
输出
对每个后序表达式，输出其等价的队列表达式。
'''

#2200015507 王一粟
class Node:
    def __init__(self,val):
        self.value = val
        self.left = None
        self.right = None

def in_level(root):
    mystack = [root]
    express = []
    while mystack:
        current_node = mystack.pop(0)
        express.append(current_node.value)
        if current_node.left:
            mystack.append(current_node.left)
            mystack.append(current_node.right)
    return "".join(reversed(express))

n = int(input())
for _ in range(n):
    s = input()
    stack = []
    for char in s:
        if char.islower():
            my_node = Node(char)
            stack.append(my_node)
        else:
            my_node = Node(char)
            my_node.right = stack.pop()
            my_node.left = stack.pop()
            stack.append(my_node)
    root_node = stack.pop()
    print(in_level(root_node))








