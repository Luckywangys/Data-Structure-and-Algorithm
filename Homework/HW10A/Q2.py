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
def post(pre,middle):
    if pre == "":
        return ""
    root = pre[0]
    middle_id = middle.find(root)
    left_mid = middle[:middle_id]
    right_mid = middle[middle_id+1:]
    left_pre = pre[1:len(left_mid)+1]
    right_pre = pre[len(left_mid)+1:]
    return post(left_pre,left_mid)+post(right_pre,right_mid)+root
while True:
    try:
        pre,middle = input().split()
        print(post(pre,middle))
    except:
        break