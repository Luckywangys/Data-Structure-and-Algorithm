'''
描述
有一棵 k 层的满二叉树（一共有2k-1个节点，且从上到下从左到右依次编号为1, 2, ..., 2k-1），最开始每个节点的重量均为0。请编程实现如下两种操作：
1 x y：给以 x 为根的子树的每个节点的重量分别增加 y（ y 是整数且绝对值不超过100）
2 x：查询（此时的）以 x 为根的子树的所有节点重量之和
输入
输入有n+1行。第一行是两个整数k, n，分别表示满二叉树的层数和操作的个数。接下来n行，每行形如1 x y或2 x，表示一个操作。
k<=15（即最多32767个节点），n<=50000。
输出
输出有若干行，对每个查询操作依次输出结果，每个结果占一行。
'''

#2200015507 王一粟
import math
def multiple(idx,k):
    level = int(math.log2(idx))
    return 2**(k-level)-1
k,n = [int(i) for i in input().split()]
multi_list = [0]*(2**k)
add = [0]*(2**k)
down_weight_list = [0]*(2**k)
for _ in range(n):
    s = [int(i) for i in input().split()]
    if s[0] == 1:
        now_type,root,add_weight = s
        if multi_list[root] == 0:
            multi_list[root] = multiple(root, k)
        multi = multi_list[root]*add_weight
        add[root] += add_weight
        current = root
        while current:
            down_weight_list[current] += multi
            current = current//2
    else:
        now_type,root = s
        result = down_weight_list[root]
        current = root//2
        if multi_list[root] == 0:
            multi_list[root] = multiple(root, k)
        multi = multi_list[root]
        while current:
            result += add[current]*multi
            current = current //2
        print(result)