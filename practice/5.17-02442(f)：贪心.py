'''
描述
Given m sequences, each contains n non-negative integer. Now we may select one number from each sequence to form a sequence with m integers. It's clear that we may get n ^ m this kind of sequences. Then we can calculate the sum of numbers in each sequence, and get n ^ m values. What we need is the smallest n sums. Could you help us?
输入
The first line is an integer T, which shows the number of test cases, and then T test cases follow. The first line of each case contains two integers m, n (0 < m <= 100, 0 < n <= 2000). The following m lines indicate the m sequence respectively. No integer in the sequence is greater than 10000.
输出
For each test case, print a line with the smallest n sums in increasing order, which is separated by a space.
'''

#2200015507 王一粟
import heapq
for _ in range(int(input())):
    m,n = [int(i) for i in input().split()]
    ans = sorted([int(i) for i in input().split()])
    for i in range(m-1):
        l = sorted([int(i) for i in input().split()])
        heap,res,cnt = [],[],0
        for j in range(n):
            heapq.heappush(heap,(ans[j]+l[0],j,0))
        while True:
            num,x,y = heapq.heappop(heap)
            res.append(num)
            cnt += 1
            if cnt == n:
                break
            heapq.heappush(heap,(ans[x]+l[y+1],x,y+1))
        ans = res
    print(*ans)

