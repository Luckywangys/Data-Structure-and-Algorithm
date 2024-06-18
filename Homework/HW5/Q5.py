'''
描述
假设二叉树的节点里包含一个大写字母，每个节点的字母都不同。
给定二叉树的中序遍历序列和后序遍历序列(长度均不超过26)，请输出该二叉树的前序遍历序列。
输入
2行，均为大写字母组成的字符串，表示一棵二叉树的中序遍历序列与后序遍历排列。
输出
表示二叉树的前序遍历序列。
'''

#2200015507 王一粟
def pre_order(in_order,post_order):
    if in_order == []:
        return []
    root = post_order[-1]
    index = in_order.index(root)
    left_in_order = in_order[:index]
    right_in_order = in_order[index+1:]
    left_post_order = post_order[:len(left_in_order)]
    right_post_order = post_order[len(left_in_order):-1]
    result_list = [root] + pre_order(left_in_order,left_post_order)+pre_order(right_in_order,right_post_order)
    return result_list
in_order = list(input())
post_order = list(input())
print("".join(pre_order(in_order,post_order)))