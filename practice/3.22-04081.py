'''
描述
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

root = Node()
s = input()
stack = [root]
general_height = 0
current_height = 0
for element in s:
    if element == "d":
        current_node = Node()
        stack[-1].child.append(current_node)
        stack.append(current_node)
        current_height += 1
    else:
        if current_height > general_height:
            general_height = current_height
        current_height -= 1
        stack.pop()
if current_height > general_height:
    general_height = current_height
def height(node):
    if node.child == []:
        return 0
    else:
        max_num = 0
        for index,element in enumerate(node.child):
            current_num = index+1+height(element)
            if current_num > max_num:
                max_num = current_num
        return max_num
modify_height = height(root)
print(f"{general_height} => {modify_height}")