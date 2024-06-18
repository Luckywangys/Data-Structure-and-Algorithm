'''
描述
二叉搜索树在动态查表中有特别的用处，一个无序序列可以通过构造一棵二叉搜索树变成一个有序序列，
构造树的过程即为对无序序列进行排序的过程。每次插入的新的结点都是二叉搜索树上新的叶子结点，在进行
插入操作时，不必移动其它结点，只需改动某个结点的指针，由空变为非空即可。

     这里，我们想探究二叉树的建立和层次输出。

输入
只有一行，包含若干个数字，中间用空格隔开。（数字可能会有重复，对于重复的数字，只计入一个）
输出
输出一行，对输入数字建立二叉搜索树后进行按层次周游的结果。
'''
#2200015507 王一粟
class Node:
    def __init__(self):
        self.val = None
        self.left = None
        self.right = None
    def setvalue(self,value):
        self.val = value
    def getvalue(self):
        return self.val

def level_express(mynode):
    result_list = []
    stack = [mynode]
    while stack:
        current_node = stack.pop(0)
        result_list.append(current_node.getvalue())
        if current_node.left:
            stack.append(current_node.left)
        if current_node.right:
            stack.append(current_node.right)
    return result_list

origin_list = [int(i) for i in input().split()]
cnt = 0
for num in origin_list:
    operate_node = Node()
    operate_node.setvalue(num)
    if cnt == 0:
        cnt = 1
        root_node = operate_node
        continue
    current_node = root_node
    while True:
        if current_node.getvalue() == num:
            break
        elif current_node.getvalue() < num:
            parent_node = current_node
            current_node = current_node.right
            if current_node is None:
                parent_node.right = operate_node
                break
        else:
            parent_node = current_node
            current_node = current_node.left
            if current_node is None:
                parent_node.left = operate_node
                break
end_result = level_express(root_node)
print(" ".join(str(i) for i in end_result))