'''
描述
假设二叉树的节点里包含一个大写字母，每个节点的字母都不同。
给定二叉树的前序遍历序列和中序遍历序列(长度均不超过26)，请输出该二叉树的后序遍历序列
输入
多组数据
每组数据2行，第一行是前序遍历序列，第二行是中序遍历序列
输出
对每组序列建树，输出该树的后序遍历序列
'''

#2200015507 王一粟
def post_order(pre_order,in_order):
    if len(pre_order) == 0:
        return []
    root = pre_order[0]
    root_index = in_order.index(root)
    left_in_order = in_order[:root_index]
    right_in_order = in_order[root_index+1:]
    left_pre_order = pre_order[1:len(left_in_order)+1]
    right_pre_order = pre_order[len(left_in_order)+1:]
    result = post_order(left_pre_order,left_in_order) + post_order(right_pre_order,right_in_order) + [root]
    return result
while True:
    try:
        pre_order = list(input())
        in_order = list(input())
        result_list = post_order(pre_order,in_order)
        print("".join(result_list))
    except:
        break