'''
描述
生态文明建设是关系中华民族永续发展的根本大计。近年来，为了响应环保号召，商家们研制出了环保烟花。这类烟花在烟花配方中不采用含有重金属和硫元素的物质，从而减少了硫化物的生成。
为了庆祝院庆，A大学计算机院燃放了一批环保烟花。从正面看，烟花的构成了二叉树的形状。那么从侧面看，烟花又是什么样子的呢？
对于一个二叉树形状的烟花，它有N个节点，每个节点都有一个1~N之间的颜色编号，不同节点的编号互不相同。除了根节点的编号固定为1，其他节点的编号都是随机分配的。
我们需要按照从顶部到底部的顺序，输出从右侧能看到的节点的颜色编号，即输出广度优先搜索中每一层最后一个节点。
输入
输入共N+1行。
第1行为一个整数N（1<=N<=1000），表示二叉树中的节点个数。这N个节点的颜色编号分别为1到N，其中1号节点为根节点。
接下来N行每行有两个整数，分别为1~N号节点的左子节点和右子节点的颜色编号，如果子节点为空，则用-1表示。
输出
按从顶到底的顺序，输出从右侧看二叉树看到的各个节点的颜色编号（即广度优先搜索中每一层最后一个节点），每个编号之间用空格隔开。
'''

#2200015507 王一粟
from collections import deque
class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.height = None

n = int(input())
node = [0] + [Node() for i in range(n)]
for i in range(1,n+1):
    l,r = map(int,input().split())
    if l != -1:
        node[i].left = l
    if r != -1:
        node[i].right = r
node[1].height = 0
prev = -1
h = 0
queue = deque([1])
result = []
while queue:
    idx = queue.popleft()
    if node[idx].height > h:
        result.append(prev)
        h += 1
    if node[idx].left:
        node[node[idx].left].height = node[idx].height + 1
        queue.append(node[idx].left)
    if node[idx].right:
        node[node[idx].right].height = node[idx].height + 1
        queue.append(node[idx].right)
    prev = idx
result.append(prev)
print(*result)