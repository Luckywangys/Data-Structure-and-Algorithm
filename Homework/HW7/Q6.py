'''
描述
请你对输入的树做遍历。遍历的规则是：遍历到每个节点时，按照该节点和所有子节点的值从小到大进行遍历
输入
第一行：节点个数n (n<500)
接下来的n行：第一个数是此节点的值，之后的数分别表示它的所有子节点的值。每个数之间用空格隔开。如果没有子节点，该行便只有一个数。
输出
输出遍历结果，一行一个节点的值。
'''

#2200015507 王一粟
class Node:
    def __init__(self,val):
        self.val = val
        self.child = []
    def chil(self):
        return self.child
    def va(self):
        return self.val
n = int(input())
data_list = []
node_dict = {}
for i in range(n):
    mylist = [int(i) for i in input().split()]
    node_dict[mylist[0]] = [Node(mylist[0]),1]
    data_list.append(mylist)
for p in data_list:
    for i in p[1:]:
        node_dict[p[0]][0].child.append(node_dict[i][0])
        node_dict[i][1] = 0
for element,k in node_dict.items():
    if k[1] == 1:
        root = k[0]
        break
def parse(root):
    result = []
    if root.chil() == []:
        return [root.va()]

    operate = sorted(root.chil()+[root],key = lambda x:x.va())
    for element in operate:
        if element == root:
            result.append(root.va())
        else:
            result += parse(element)
    return result
t = parse(root)
for i in t:
    print(int(i))