'''
描述
Farmer John wants to repair a small length of the fence around the pasture. He measures the fence and finds that he needs N (1 ≤ N ≤ 20,000) planks of wood, each having some integer length Li (1 ≤ Li ≤ 50,000) units. He then purchases a single long board just long enough to saw into the N planks (i.e., whose length is the sum of the lengths Li). FJ is ignoring the "kerf", the extra length lost to sawdust when a sawcut is made; you should ignore it, too.
FJ sadly realizes that he doesn't own a saw with which to cut the wood, so he mosies over to Farmer Don's Farm with this long board and politely asks if he may borrow a saw.
Farmer Don, a closet capitalist, doesn't lend FJ a saw but instead offers to charge Farmer John for each of the N-1 cuts in the plank. The charge to cut a piece of wood is exactly equal to its length. Cutting a plank of length 21 costs 21 cents.
Farmer Don then lets Farmer John decide the order and locations to cut the plank. Help Farmer John determine the minimum amount of money he can spend to create the N planks. FJ knows that he can cut the board in various different orders which will result in different charges since the resulting intermediate planks are of different lengths.
输入
Line 1: One integer N, the number of planks
Lines 2..N+1: Each line contains a single integer describing the length of a needed plank
输出
Line 1: One integer: the minimum amount of money he must spend to make N-1 cuts
'''

#2200015507 王一粟
import heapq
n = int(input())
mylist = []
for _ in range(n):
    mylist.append(int(input()))
result = 0
heapq.heapify(mylist)
cnt = 0
while cnt < n-1:
    cnt += 1
    a1 = heapq.heappop(mylist)
    a2 = heapq.heappop(mylist)
    result = result + a1 + a2
    heapq.heappush(mylist,a1+a2)
print(result)