'''
描述
可以用括号嵌套的方式来表示一棵树。表示方法如下：
1) 如果一棵树只有一个结点，则该树就用一个大写字母表示，代表其根结点。
2) 如果一棵树有子树，则用“树根(子树1,子树2,...,子树n)”的形式表示。树根是一个大写字母,子树之间用逗号隔开，没有空格。子树都是用括号嵌套法表示的树。
给出一棵不超过26个结点的树的括号嵌套表示形式，请输出其前序遍历序列和后序遍历序列。
输入
一行，一棵树的括号嵌套表示形式
输出
两行。第一行是树的前序遍历序列，第二行是树的后序遍历序列
'''

#2200015507 王一粟
class Node:
    def __init__(self,value):
        self.val = value
        self.child = []
    def get_value(self):
        return self.val
    def get_child(self):
        return self.child

s = input()
root_node = Node(s[0])
stack = []
stack.append(root_node)
cnt = 0
for char in s[1:]:
    if char == "(":
        parent_node = stack[-1]
    elif char == ")":
        stack.pop()
    elif char == ",":
        stack.pop()
        parent_node = stack[-1]
    else:
        my_node = Node(char)
        parent_node.child.append(my_node)
        stack.append(my_node)
def pre_order(root):
    if root.get_child() == []:
        return [root.get_value()]
    else:
        result_list = [root.get_value()]
        for element in root.get_child():
            result_list.extend(pre_order(element))
        return result_list
def post_order(root):
    if root.get_child() == []:
        return [root.get_value()]
    else:
        result_list = []
        for element in root.get_child():
            result_list.extend(post_order(element))
        result_list.append(root.get_value())
        return result_list
print("".join(pre_order(root_node)))
print("".join(post_order(root_node)))