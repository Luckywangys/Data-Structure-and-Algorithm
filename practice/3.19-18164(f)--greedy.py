'''
描述
小张要将一根长度为L的绳子剪成N段。准备剪的绳子的长度为L1,L2,L3...,LN，未剪的绳子长度恰好为剪后所有绳子长度的和。
每次剪断绳子时，需要的开销是此段绳子的长度。
比如，长度为10的绳子要剪成长度为2,3,5的三段绳子。长度为10的绳子切成5和5的两段绳子时，开销为10。再将5切成长度为2和3的绳子，开销为5。因此总开销为15。
请按照目标要求将绳子剪完最小的开销是多少。
已知，1<=N <= 20000，0<=Li<= 50000
输入
第一行：N，将绳子剪成的段数。
第二行：准备剪成的各段绳子的长度。
输出
最小开销
'''

#2200015507 王一粟
import heapq
n = int(input())
mylist = [int(i) for i in input().split()]
heapq.heapify(mylist)
total = 0
a = heapq.heappop(mylist)
while mylist:
    b = heapq.heappop(mylist)
    total += a+b
    heapq.heappush(mylist,a+b)
    a = heapq.heappop(mylist)
print(total)