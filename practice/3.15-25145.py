'''
描述
一棵二叉树，结点都是大写英文字母，且不重复。
给出它的中序遍历序列和后序遍历序列，求其按层次遍历的序列
输入
第一行是整数n, n <=30，表示有n棵二叉树
接下来每两行代表一棵二叉树，第一行是其中序遍历序列，第二行是后序遍历序列
输出
对每棵二叉树输出其按层次遍历序列
'''

#2200015507 王一粟
class Node:
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None
    def get_val(self):
        return self.val
def parse(in_order,post_order):
    if in_order:
        root_node = Node(post_order[-1])
        index_in_order = in_order.index(post_order[-1])
        left_in_order = None if index_in_order == 0 else in_order[:index_in_order]
        right_in_order = None if index_in_order == len(in_order) - 1 else in_order[index_in_order+1:]
        left_post_order = None if index_in_order == 0 else post_order[:len(left_in_order)]
        right_post_order = None if index_in_order == len(in_order) - 1 else post_order[-1-len(right_in_order):-1]
        root_node.left = parse(left_in_order,left_post_order)
        root_node.right = parse(right_in_order,right_post_order)
        return root_node
n = int(input())
for _ in range(n):
    in_order = list(input())
    post_order = list(input())
    root = parse(in_order,post_order)
    stack = [root]
    express = []
    while stack:
        current_node = stack.pop(0)
        express.append(current_node.get_val())
        if current_node.left:
            stack.append(current_node.left)
        if current_node.right:
            stack.append(current_node.right)
    print("".join(express))








