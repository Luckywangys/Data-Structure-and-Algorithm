'''
描述
为了促进蚂蚁家族身体健康，提高蚁族健身意识，蚂蚁王国举行了越野跑。假设越野跑共有N个蚂蚁参加，在一条笔直的道路上进行。N个蚂蚁在起点处站成一列，相邻两个蚂蚁之间保持一定的间距。比赛开始后，N个蚂蚁同时沿着道路向相同的方向跑去。换句话说，这N个蚂蚁可以看作x轴上的N个点，在比赛开始后，它们同时向X轴正方向移动。假设越野跑的距离足够远，这N个蚂蚁的速度有的不相同有的相同且保持匀速运动，那么会有多少对参赛者之间发生“赶超”的事件呢？此题结果比较大，需要定义long long类型。请看备注。
输入
第一行1个整数N。
第2… N +1行：N 个非负整数，按从前到后的顺序给出每个蚂蚁的跑步速度。对于50%的数据，2<=N<=1000。对于100%的数据，2<=N<=100000。
输出
一个整数，表示有多少对参赛者之间发生赶超事件。
提示
考虑归并排序的思想。
'''

#2200015507 王一粟
def merge_sort(mylist):
    length = len(mylist)
    if length == 1:
        return 0,mylist
    k = length//2
    left_inverse,left_list = merge_sort(mylist[:k])
    right_inverse,right_list = merge_sort(mylist[k:])
    i,j = 0,0
    result_list = []
    result = 0
    while i < k and j < length-k:
        if left_list[i] < right_list[j]:
            result_list.append(right_list[j])
            result += k-i
            j += 1
        else:
            result_list.append(left_list[i])
            i += 1
    if i == k:
        result_list.extend(right_list[j:])
    else:
        result_list.extend(left_list[i:])
    return left_inverse+right_inverse+result,result_list

n = int(input())
wait_list = []
for _ in range(n):
    wait_list.append(int(input()))
inverse,the_list = merge_sort(wait_list)
print(inverse)