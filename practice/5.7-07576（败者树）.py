'''
描述
给定一个整数数组，要求对数组中的元素构建败方树（数组相邻元素两两比较，从第一个元素开始）。之后修改数组中的元素，要求输出初始构建以及修改后得到的败方树的所有内部结点代表的整数(从左到右从上到下输出）
输入
第一行为数组的元素个数n和修改的次数m。
第二行为n个整数，即数组的元素。
接下来m行代表m次修改操作，每次操作修改数组中的一个元素，每一行包括两个整数，第一个为被修改元素在数组中的标号，第二个为修改之后的元素值。
输出
输出m+1行。
第一行为初始构建的败方树的所有内部结点代表的整数(按照树的结点从左到右从上到下的顺序输出）
接下来m行为接下来m次修改后得到的败方树的所有内部结点代表的整数(按照树的结点从左到右从上到下的顺序输出）
'''
#2200015507 王一粟
from collections import deque
class Node:
    def __init__(self,data,win):
        self.data = data
        self.win = win
        self.left = None
        self.right = None
def buildtree(list1):
    stack = deque()
    for i in list1:
        stack.append(Node(i,i))
    while len(stack) > 1:
        a = stack.popleft()
        b = stack.popleft()
        if a.win < b.win:
            c = Node(b.win,a.win)
        else:
            c = Node(a.win,b.win)
        c.left = a
        c.right = b
        stack.append(c)
    root = Node(stack[0].win,stack[0].win)
    root.left = stack[0]
    return root
def show(n,root):
    stack = deque()
    stack.append(root)
    ans = []
    while stack:
        if len(ans) == n:
            print(*ans)
            return
        a = stack.popleft()
        ans.append(a.data)
        if a.left:
            stack.append(a.left)
        if a.right:
            stack.append(a.right)
n,m = map(int,input().split())
list1 = list(map(int,input().split()))
root = buildtree(list1)
show(n,root)
for _ in range(m):
    pos,val = map(int,input().split())
    list1[pos] = val
    show(n,buildtree(list1))