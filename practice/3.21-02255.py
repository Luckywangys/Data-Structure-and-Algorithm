'''
描述
给定一棵二叉树的前序遍历和中序遍历的结果，求其后序遍历。
输入
输入可能有多组，以EOF结束。
每组输入包含两个字符串，分别为树的前序遍历和中序遍历。每个字符串中只包含大写字母且互不重复。
输出
对于每组输入，用一行来输出它后序遍历结果。
'''

#2200015507 王一粟
def post(pre_order,in_order):
    if pre_order == []:
        return []
    root = pre_order[0]
    root_index = in_order.index(root)
    left_in_order = in_order[:root_index]
    right_in_order = in_order[root_index+1:]
    left_pre_order = pre_order[1:len(left_in_order)+1]
    right_pre_order = pre_order[len(left_in_order)+1:]
    return post(left_pre_order,left_in_order) + post(right_pre_order,right_in_order)+[root]

while True:
    try:
        pre_order, in_order = input().split()
        pre_order = list(pre_order)
        in_order = list(in_order)
        result = post(pre_order, in_order)
        print("".join(result))
    except:
        break