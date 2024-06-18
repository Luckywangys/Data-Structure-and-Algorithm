'''
描述
Freda报名参加了学校的越野跑。越野跑共有N人参加，在一条笔直的道路上进行。这N个人在起点处站成一列，相邻两个人之间保持一定的间距。比赛开始后，这N个人同时沿着道路向相同的方向跑去。换句话说，这N个人可以看作x轴上的N个点，在比赛开始后，它们同时向x轴正方向移动。
假设越野跑的距离足够远，这N个人的速度各不相同且保持匀速运动，那么会有多少对参赛者之间发生“赶超”的事件呢？
输入
第一行1个整数N。
第二行为N 个非负整数，按从前到后的顺序给出每个人的跑步速度。
对于50%的数据，2<=N<=1000。
对于100%的数据，2<=N<=100000。
输出
一个整数，表示有多少对参赛者之间发生赶超事件。
'''
#2200015507 王一粟
n = int(input())
operate_list = [int(i) for i in input().split()]
def merge(mylist):
    m = len(mylist)
    if m == 1:
        return mylist,0
    k = m//2
    left_side,left_inverse = merge(mylist[:k])
    right_side,right_inverse = merge(mylist[k:])
    result_list = []
    i = 0
    j = 0
    result = 0
    while i<k and j<m-k:
        if left_side[i] < right_side[j]:
            result_list.append(right_side[j])
            result += k-i
            j+=1
        else:
            result_list.append(left_side[i])
            i+=1
    if i==k:
        result_list.extend(right_side[j:])
    else:
        result_list.extend(left_side[i:])
    return result_list,result+left_inverse+right_inverse

end_list,inverse_num = merge(operate_list)
print(inverse_num)














