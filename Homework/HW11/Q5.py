'''
描述
依次读入一个整数序列，每当已经读入的整数个数为奇数时，输出已读入的整数构成的序列的中位数。
输入
第一行输入一个整数 T（1<=T<=100），代表后面数据集的个数。
接下来每行一个数据集，包含 M 个空格分隔的整数。1<=M<=99999 且所有 M 相加之和不超过500000。
输出
对于每个数据集输出两行，第一行输出中位数的个数N。
第二行输出空格分隔的N个整数，表示中位数。
'''

#2200015507 王一粟
import heapq
for _ in range(int(input())):
    mylist = [int(i) for i in input().split()]
    n = len(mylist)
    if n == 1 or n==2:
        print(1)
        print(mylist[0])
        continue
    print((n+1)//2)
    mid = mylist[0]
    result = [mid]
    left = []
    right = []
    num1, num2 = mylist[1], mylist[2]
    if num2 < num1:
        num1, num2 = num2, num1
    if num1 <= mid <= num2:
        result.append(mid)
        left.append(-num1)
        right.append(num2)
    elif num2 < mid:
        result.append(num2)
        left.append(-num1)
        right.append(mid)
        mid = num2
    else:
        result.append(num1)
        left.append(-mid)
        right.append(num2)
        mid = num1
    for i in range(3,n-1,2):
        num1,num2 = mylist[i],mylist[i+1]
        if num2<num1:
            num1,num2 = num2,num1
        if num1<=mid<=num2:
            heapq.heappush(left,-num1)
            heapq.heappush(right,num2)
            result.append(mid)
        elif num2 < mid:
            heapq.heappush(right,mid)
            heapq.heappush(left,-num1)
            wait_for_mid = -heapq.heappop(left)
            if num2<wait_for_mid:
                mid = wait_for_mid
            else:
                mid = num2
                num2 = wait_for_mid
            heapq.heappush(left,-num2)
            result.append(mid)
        else:
            heapq.heappush(left,-mid)
            heapq.heappush(right,num2)
            wait_for_mid = heapq.heappop(right)
            if wait_for_mid < num1:
                mid = wait_for_mid
            else:
                mid = num1
                num1 = wait_for_mid
            heapq.heappush(right,num1)
            result.append(mid)
    print(" ".join(str(i) for i in result))