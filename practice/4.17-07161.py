'''
描述
对于树和森林等非线性结构，我们往往需要将其序列化以便存储。有一种树的存储方式称为带度数的层次序列。我们可以通过层次遍历的方式将森林序列转化为多个带度数的层次序列。
两棵树的层次遍历序列分别为：C E F G K H J / D X I
每个结点对应的度数为：3 3 0 0 0 0 0 / 2 0 0
我们将以上序列存储起来，就可以在以后的应用中恢复这个森林。在存储中，我们可以将第一棵树表示为C 3 E 3 F 0 G 0 K 0 H 0 J 0，第二棵树表示为D 2 X 0 I 0。
现在有一些通过带度数的层次遍历序列存储的森林数据，为了能够对这些数据进行进一步处理，首先需要恢复他们。
输入
输入数据的第一行包括一个正整数n，表示森林中非空的树的数目。
随后的 n 行，每行给出一棵树的带度数的层次序列。
树的节点名称为A-Z的单个大写字母。
输出
输出包括一行，输出对应森林的后根遍历序列。
'''
#2200015507 王一粟
from collections import deque
class Node:
    def __init__(self,val):
        self.val = val
        self.child = []
    def get(self):
        return self.val

def post(node):
    answer = []
    for element in node.child:
        answer.extend(post(element))
    answer = answer + [node.get()]
    return answer
n = int(input())
result = []
for i in range(n):
    mylist = input().split()
    root = Node(mylist[0])
    degrees = int(mylist[1])
    queue = deque([[root,degrees,0]])
    if degrees == 0:
        result.append(mylist[0])
        continue
    for idx in range(2,len(mylist),2):
        name,degree = mylist[idx],int(mylist[idx+1])
        current_node = Node(name)
        queue[0][0].child.append(current_node)
        queue[0][2] += 1
        if queue[0][2] == queue[0][1]:
            queue.popleft()
        if degree != 0:
            queue.append([current_node,degree,0])
    result.extend(post(root))
print(" ".join(result))






