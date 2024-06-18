'''
描述
给定一棵二叉树，在二叉树上执行两个操作：
1. 节点交换
把二叉树的两个节点交换。
2. 前驱询问
询问二叉树的一个节点对应的子树最左边的节点。
输入
第一行输出一个整数t(t <= 100)，代表测试数据的组数。
对于每组测试数据，第一行输入两个整数n m，n代表二叉树节点的个数，m代表操作的次数。
随后输入n行，每行包含3个整数X Y Z，对应二叉树一个节点的信息。X表示节点的标识，Y表示其左孩子的标识，Z表示其右孩子的标识。
再输入m行，每行对应一次操作。每次操作首先输入一个整数type。
当type=1，节点交换操作，后面跟着输入两个整数x y，表示将标识为x的节点与标识为y的节点交换。输入保证对应的节点不是祖先关系。
当type=2，前驱询问操作，后面跟着输入一个整数x，表示询问标识为x的节点对应子树最左的孩子。
1<=n<=100，节点的标识从0到n-1，根节点始终是0.
m<=100
输出
对于每次询问操作，输出相应的结果。
'''

#2200015507 王一粟
class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.child = self
        self.parent = None
        self.parent_attribute = None
    def get(self):
        return self.val
def find(node):
    if node.child == node:
        return node
    else:
        node.child = find(node.left)
        return node.child
for _ in range(int(input())):
    n,m = [int(i) for i in input().split()]
    node_list = [Node(i) for i in range(n)]
    for i in range(n):
        idx,left_idx,right_idx = [int(i) for i in input().split()]
        if left_idx != -1:
            node_list[idx].left = node_list[left_idx]
            node_list[idx].child = node_list[left_idx].child
            node_list[left_idx].parent = node_list[idx]
            node_list[left_idx].parent_attribute = "left"
        if right_idx != -1:
            node_list[idx].right = node_list[right_idx]
            node_list[right_idx].parent = node_list[idx]
            node_list[right_idx].parent_attribute = "right"
    for i in range(m):
        s = [int(i) for i in input().split()]
        if s[0] == 1:
            use_type,x,y = s
            x = node_list[x]
            y = node_list[y]
            if x.parent_attribute == "left":
                x.parent.left = y
                current_node = x.parent
                x.parent.child = y.child
                while True:
                    if current_node.parent_attribute == "left":
                        current_node.parent.child = y.child
                        current_node = current_node.parent
                    else:
                        break
            else:
                x.parent_right = y
            if y.parent_attribute == "left":
                y.parent.left = x
                current_node = y.parent
                y.parent.child = x.child
                while True:
                    if current_node.parent_attribute == "left":
                        current_node.parent_child = x.child
                        current_node = current_node.parent
                    else:
                        break
            else:
                y.parent_right = x
            x.parent,y.parent = y.parent,x.parent
            x.parent_attribute,y.parent_attribute = y.parent_attribute,x.parent_attribute
        else:
            use_type,x = s
            print(find(node_list[x]).get())