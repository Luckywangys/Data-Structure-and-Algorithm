'''
描述
众所周知，任何一个表达式，都可以用一棵表达式树来表示。例如，表达式a+b*c，可以表示为如下的表达式树：
   +
  / \
a   *
    / \
    b c
现在，给你一个中缀表达式，这个中缀表达式用变量来表示（不含数字），请你将这个中缀表达式用表达式二叉树的形式输出出来。
输入
输入分为三个部分。
第一部分为一行，即中缀表达式(长度不大于50)。中缀表达式可能含有小写字母代表变量（a-z），也可能含有运算符（+、-、*、/、小括号），不含有数字，也不含有空格。
第二部分为一个整数n(n < 10)，表示中缀表达式的变量数。
第三部分有n行，每行格式为C　x，C为变量的字符，x为该变量的值。
输出
输出分为三个部分，第一个部分为该表达式的逆波兰式，即该表达式树的后根遍历结果。占一行。
第二部分为表达式树的显示，如样例输出所示。如果该二叉树是一棵满二叉树，则最底部的叶子结点，分别占据横坐标的第1、3、5、7……个位置（最左边的坐标是1），然后它们的父结点的横坐标，在两个子结点的中间。如果不是满二叉树，则没有结点的地方，用空格填充（但请略去所有的行末空格）。每一行父结点与子结点中隔开一行，用斜杠（/）与反斜杠（\）来表示树的关系。/出现的横坐标位置为父结点的横坐标偏左一格，\出现的横坐标位置为父结点的横坐标偏右一格。也就是说，如果树高为m，则输出就有2m-1行。
第三部分为一个整数，表示将值代入变量之后，该中缀表达式的值。需要注意的一点是，除法代表整除运算，即舍弃小数点后的部分。同时，测试数据保证不会出现除以0的现象。
'''
#2200015507 王一粟
from collections import deque
class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.level = 1
    def get(self):
        return self.val
    def lev(self):
        return self.level
in_express = input()
calculate = ""
post_express = []
stack = []
n = int(input())
nums = {}
for _ in range(n):
    alpha,num = input().split()
    nums[alpha] = num
for element in in_express:
    if element == "(":
        stack.append(element)
        calculate += element
    elif element == ")":
        calculate += element
        while True:
            new = stack.pop()
            if new == "(":
                break
            post_express.append(new)
    elif element in "+-":
        calculate += element
        while True:
            if stack and stack[-1] in "+-*/":
                post_express.append(stack.pop())
            else:
                stack.append(element)
                break
    elif element in "*/":
        if element == "/":
            calculate += "//"
        else:
            calculate += "*"
        while True:
            if stack and stack[-1] in "*/":
                post_express.append(stack.pop())
            else:
                stack.append(element)
                break
    else:
        calculate += nums[element]
        post_express.append(element)
while stack:
    post_express.append(stack.pop())
print("".join(post_express))
queue = deque()
for element in post_express:
    if element in "+-*/":
        current_node = Node(element)
        current_node.right = queue.pop()
        current_node.left = queue.pop()
        current_node.level = 1+max(current_node.left.level,current_node.right.level)
        queue.append(current_node)
    else:
        current_node = Node(element)
        queue.append(current_node)
root = queue[0]
total_level = root.lev()
total_length = 2**total_level
root_par = total_length//2
print(" "*(root_par-1) + root.get())
queue = deque([root])
for level in range(2,total_level+1):
    root_par = root_par // 2
    branch = ""
    level_express = ""
    for idx in range(1,2**(level-1)+1,2):
        parent_node = queue.popleft()
        if parent_node.left is None:
            level_express += root_par*4*" "
            branch += " "*(4*root_par)
            queue.append(Node(1))
            queue.append(Node(1))
        else:
            left_node = parent_node.left
            right_node = parent_node.right
            branch = branch + (2*root_par-2) * " " + "/" + " " + "\\" + (2*root_par-1) * " "
            level_express = level_express + " "*(root_par-1) + left_node.get() + " "*(2*root_par-1) + right_node.get() + " "*root_par
            queue.append(left_node)
            queue.append(right_node)
    print(branch.rstrip())
    print(level_express.rstrip())
print(eval(calculate))