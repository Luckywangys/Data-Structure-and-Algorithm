'''
平衡二叉树的建立
将n个互不相同的正整数先后插入到一棵空的AVL树中，求最后生成的AVL树的先序序列
输入
第一行一个整数n,表示AVL树的结点个数；
第二行n个整数，表示插入序列
输出
n个整数，表示先序遍历序列，中间用空格隔开，行末不允许有多余的空格
'''
#2200015507 王一粟
class Node:
    def __init__(self,val):
        self.value = val
        self.left = None
        self.right = None
        self.height = 1
class AVL:
    def __init__(self):
        self.root = None
    def insert(self,value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.root =self._insert(self.root,value)
    def _get_height(self,node):
        if node is None:
            return 0
        return 1+max(self._get_height(node.left),self._get_height(node.right))

    def _get_balance(self,node):
        return self._get_height(node.left)-self._get_height(node.right)
    def _rotate_right(self,node):
        origin_root = node
        new_root = origin_root.left
        new_root_origin_right = new_root.right
        new_root.right = origin_root
        origin_root.left = new_root_origin_right
        new_root.height = 1+max(self._get_height(new_root.right),self._get_height(new_root.left))
        origin_root.height = 1+max(self._get_height(origin_root.left),self._get_height(origin_root.right))
        return new_root
    def _rotate_left(self,node):
        origin_root = node
        new_root = origin_root.right
        new_root_origin_left = new_root.left
        new_root.left = origin_root
        origin_root.right = new_root_origin_left
        new_root.height = 1+max(self._get_height(new_root.right),self._get_height(new_root.left))
        origin_root.height = 1 + max(self._get_height(origin_root.left), self._get_height(origin_root.right))
        return new_root
    def _insert(self,node,value):
        if node is None:
            return Node(value)
        if node.value > value:
            node.left = self._insert(node.left,value)
        else:
            node.right = self._insert(node.right,value)
        node.height = self._get_height(node)
        balance = self._get_balance(node)
        if balance > 1: #左树不平衡
            if value<node.left.value: #LL,右旋
                return self._rotate_right(node)
            else: #LR,左旋+右旋
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)
        if balance < -1: #右树不平衡
            if value>node.right.value: #RR，左旋
                return self._rotate_left(node)
            else: #RL，右旋+左旋
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)
        return node
    def preorder(self):
        return self._preorder(self.root)
    def _preorder(self,node):
        if node is None:
            return []
        return [node.value] + self._preorder(node.left)+self._preorder(node.right)
n = int(input())
mylist = [int(i) for i in input().split()]
avl = AVL()
for element in mylist:
    avl.insert(element)
result = avl.preorder()
print(" ".join(str(i) for i in result))