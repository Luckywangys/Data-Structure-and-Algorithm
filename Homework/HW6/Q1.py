'''
描述
给出一棵二叉搜索树的前序遍历，求它的后序遍历
输入
第一行一个正整数n（n<=2000）表示这棵二叉搜索树的结点个数
第二行n个正整数，表示这棵二叉搜索树的前序遍历
保证第二行的n个正整数中，1~n的每个值刚好出现一次
输出
一行n个正整数，表示这棵二叉搜索树的后序遍历
'''

#2200015507 王一粟
class Node:
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None
    def get_value(self):
        return self.val
def post_order(node):
    if node is None:
        return []
    result = []
    return post_order(node.left) + post_order(node.right) + [node.get_value()]
n = int(input())
wait_list = [int(i) for i in input().split()]
root = Node(wait_list[0])
for num in wait_list[1:]:
    current_node = root
    while True:
        if current_node.get_value() < num:
            if current_node.right:
                current_node = current_node.right
            else:
                current_node.right = Node(num)
                break
        else:
            if current_node.left:
                current_node = current_node.left
            else:
                current_node.left = Node(num)
                break
post_express = post_order(root)
print(" ".join(str(i) for i in post_express))