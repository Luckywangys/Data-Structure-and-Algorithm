'''
描述
给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
返回 滑动窗口中的最大值 。
输入
第一行包含两个整数n,k。1 <= n,k <= 10^5
第二行包含n个整数，相邻整数间以空格隔开。-10^4 <= nums[i] <= 10^4
输出
滑动窗口中的最大值,相邻整数间以空格隔开。
'''
#2200015507 王一粟
from collections import deque
n,k = [int(i) for i in input().split()]
mylist = [int(i) for i in input().split()]
max_deque = deque([[0,mylist[0]]])
for index,element in enumerate(mylist[1:k]):
    while max_deque:
        if max_deque[0][1] > element:
            break
        else:
            max_deque.popleft()
    max_deque.appendleft([index+1,element])
max_num = max_deque[-1][1]
result_list = [max_num]
for index,element in enumerate(mylist[k:]):
    while max_deque:
        if max_deque[0][1] > element:
            break
        else:
            max_deque.popleft()
    max_deque.appendleft([index+k,element])
    if index == max_deque[-1][0]:
        max_deque.pop()
    max_num = max_deque[-1][1]
    result_list.append(max_num)
print(" ".join(str(i) for i in result_list))