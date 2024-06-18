'''
描述
由于先序、中序和后序序列中的任一个都不能唯一确定一棵二叉树，所以对二叉树做如下处理，将二叉树的空结点用·补齐，如图所示。我们把这样处理后的二叉树称为原二叉树的扩展二叉树，扩展二叉树的先序和后序序列能唯一确定其二叉树。 现给出扩展二叉树的先序序列，要求输出其中序和后序序列。
输入
扩展二叉树的先序序列（全部都由大写字母或者.组成）
输出
第一行：中序序列
第二行：后序序列
'''

#2200015507 王一粟
class Node:
    def __init__(self,val):
        self.value = val
        self.left = None
        self.right = None
    def getValue(self):
        return self.value
def in_order(node):
    if node is None:
        return ""
    return in_order(node.left) + node.getValue() + in_order(node.right)
def post_order(node):
    if node is None:
        return ""
    return post_order(node.left)+post_order(node.right)+node.getValue()

s = input()
root = Node(s[0])
stack = [[root,0]]
for element in s[1:]:
    if element == ".":
        if stack[-1][1] == 0:
            stack[-1][1] = 1
        else:
            stack.pop()
    else:
        current_node = Node(element)
        if stack[-1][1] == 0:
            stack[-1][1] = 1
            stack[-1][0].left = current_node
        else:
            stack[-1][0].right = current_node
            stack.pop()
        stack.append([current_node,0])
print(in_order(root))
print(post_order(root))








