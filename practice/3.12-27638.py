'''
描述
给定一棵二叉树，求该二叉树的高度和叶子数目二叉树高度定义：从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的结点数减1为树的高度。只有一个结点的二叉树，高度是0。
输入
第一行是一个整数n，表示二叉树的结点个数。二叉树结点编号从0到n-1，根结点n <= 100 接下来有n行，依次对应二叉树的编号为0,1,2....n-1的节点。 每行有两个整数，分别表示该节点的左儿子和右儿子的编号。如果第一个（第二个）数为-1则表示没有左（右）儿子
输出
在一行中输出2个整数，分别表示二叉树的高度和叶子结点个数
'''

#2200015507 王一粟
class Node:
    def __init__(self):
        self.left = None
        self.right = None
def deep(root):
    if root.left:
        if root.right:
            return 1 + max(deep(root.left),deep(root.right))
        else:
            return 1+deep(root.left)
    else:
        if root.right:
            return 1+deep(root.right)
        else:
            return 1

def count(root):
    if root.left:
        if root.right:
            return count(root.left)+count(root.right)
        else:
            return count(root.left)
    else:
        if root.right:
            return count(root.right)
        else:
            return 1

n = int(input())
mylist = [Node() for i in range(n)]
isparent = [False]*n
for i in range(n):
    leftnum,rightnum = [int(i) for i in input().split()]
    if leftnum != -1:
        mylist[i].left = mylist[leftnum]
        isparent[leftnum] = True
    if rightnum != -1:
        mylist[i].right = mylist[rightnum]
        isparent[rightnum] = True

root_index = isparent.index(False)
height = deep(mylist[root_index]) - 1
leaf_num = count(mylist[root_index])
print(height,leaf_num)


