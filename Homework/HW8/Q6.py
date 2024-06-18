'''
描述
一棵树的镜面映射指的是对于树中的每个结点，都将其子结点反序。例如，对左边的树，镜面映射后变成右边这棵树。
我们在输入输出一棵树的时候，常常会把树转换成对应的二叉树，而且对该二叉树中只有单个子结点的分支结点补充一个虚子结点“$”，形成“伪满二叉树”。
然后对这棵二叉树进行前序遍历，如果是内部结点则标记为0，如果是叶结点则标记为1，而且虚结点也输出。
现在我们将一棵树以“伪满二叉树”的形式输入，要求输出这棵树的镜面映射的宽度优先遍历序列。
输入
输入包含一棵树所形成的“伪满二叉树”的前序遍历。
第一行包含一个整数，表示结点的数目。
第二行包含所有结点。每个结点用两个字符表示，第一个字符表示结点的编号，第二个字符表示该结点为内部结点还是外部结点，内部结点为0，外部结点为1。结点之间用一个空格隔开。
数据保证所有结点的编号都为一个小写字母。
输出
输出包含这棵树的镜面映射的宽度优先遍历序列，只需要输出每个结点的编号，编号之间用一个空格隔开。
'''

#2200015507 王一粟
from collections import deque
class Node:
    def __init__(self,val):
        self.val = val
        self.child = deque()
        self.parent = None
    def get(self):
        return self.val

n = int(input())
s = input().split()
root = Node(s[0][0])
stack = [[root,0]]
for i in s[1:]:
    value = i[0]
    property = int(i[1])
    if value != "$":
        current_node = Node(value)
        if stack[-1][-1] == 0:
            current_node.parent = stack[-1][0]
            stack[-1][0].child.appendleft(current_node)
            stack[-1][1] = 1
            if property == 0:
                stack.append([current_node,0])
        else:
            current_node.parent = stack[-1][0].parent
            stack[-1][0].parent.child.appendleft(current_node)
            stack.pop()
            if property == 0:
                stack.append([current_node,0])
    else:
        if stack[-1][-1] == 0:
            stack[-1][-1] = 1
        else:
            stack.pop()
queue = deque([root])
result = []
while queue:
    node = queue.popleft()
    result.append(node.get())
    queue.extend(node.child)
print(" ".join(result))