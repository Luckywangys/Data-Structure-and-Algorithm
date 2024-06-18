'''
描述
我们可以把由 0 和 1 组成的字符串分为三类：全 0 串称为 B 串，全 1 串称为 I 串，既含 0 又含 1 的串则称为 F 串。
FBI 树是一种二叉树，它的结点类型也包括 F 结点，B 结点和 I 结点三种。
由一个长度为 2^N 的 01 串 S 可以构造出一棵 FBI 树 T，递归的构造方法如下：
T 的根结点为 R，其类型与串 S 的类型相同；
若串 S 的长度大于 1，将串 S 从中间分开，分为等长的左右子串 S1 和 S2；由左子串 S1 构造 R 的左子树 T1，由右子串 S2 构造 R 的右子树 T2。
现在给定一个长度为 2^N 的 01 串，请用上述构造方法构造出一棵 FBI 树，并输出它的后序遍历序列。
输入
第一行是一个整数 N，0<= N <= 10。
第二行是一个长度为 2^N 的 01 串。
输出
包含一行，这一行只包含一个字符串，即 FBI 树的后序遍历序列。
'''

#2200015507 王一粟
class Node:
    def __int__(self):
        self.val = None
        self.left = None
        self.right = None
    def get(self):
        return self.val

def parse(s,n):
    if n==0:
        if s == "0":
            current_node = Node()
            current_node.val = "B"
            current_node.left,current_node.right = None,None
            return current_node
        else:
            current_node = Node()
            current_node.val = "I"
            current_node.left, current_node.right = None, None
            return current_node
    else:
        current_node = Node()
        current_node.left = parse(s[:2**(n-1)],n-1)
        current_node.right = parse(s[2**(n-1):],n-1)

        if current_node.left.val == "B" and current_node.right.val == "B":
            current_node.val = "B"
        elif current_node.left.val == "I" and current_node.right.val == "I":
            current_node.val = "I"
        else:
            current_node.val = "F"
        return current_node
def post(root):
    if root is None:
        return ""
    else:
        return post(root.left)+post(root.right)+root.get()
n = int(input())
s = input()
root = parse(s,n)
print(post(root))