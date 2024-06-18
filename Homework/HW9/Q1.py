'''
我们都知道用“左儿子右兄弟”的方法可以将一棵一般的树转换为二叉树
现在请你将一些一般的树用这种方法转换为二叉树，并输出转换前和转换后树的高度。
输入
输入是一个由“u”和“d”组成的字符串，表示一棵树的深度优先搜索信息。比如，dudduduudu可以用来表示上文中的左树，因为搜索过程为：0 Down to 1 Up to 0 Down to 2 Down to 4 Up to 2 Down to 5 Up to 2 Up to 0 Down to 3 Up to 0。
你可以认为每棵树的结点数至少为2，并且不超过10000。
输出
按如下格式输出转换前和转换后树的高度：
h1 => h2
其中，h1是转换前树的高度，h2是转换后树的高度。
'''

#2200015507 王一粟
class Node:
    def __init__(self):
        self.child = []
    def get_child(self):
        return self.child

def max_height(node):
    ma_height = -1
    for idx,child in enumerate(node.get_child()):
        height = idx + max_height(child)
        if height > ma_height:
            ma_height = height
    return ma_height+1

s = input()
root = Node()
stack = [root]
max_origin = 0
origin = 0
for element in s:
    if element == "d":
        current_node = Node()
        stack[-1].child.append(current_node)
        stack.append(current_node)
        origin = origin + 1
    else:
        max_origin = max(max_origin,origin)
        origin = origin - 1
        stack.pop()
change = max_height(root)
print(f"{max_origin} => {change}")