'''
描述
一个数字三角形。从三角形的顶部到底部有很多条不同的路径。对于每条路径，把路径上面的数加起来可以得到一个和，你的任务就是找到最大的和。
注意：路径上的每一步只能从一个数走到下一层上和它最近的左边的那个数或者右边的那个数。
输入
输入的是一行是一个整数N (1 < N <= 100)，给出三角形的行数。下面的N行给出数字三角形。数字三角形上的数的范围都在0和100之间。
输出
输出最大的和。
'''

#2200015507 王一粟
mylist = []
n = int(input())
for _ in range(n):
    num_list = [int(i) for i in input().split()]
    mylist.append(num_list)
dp = [[0 for _ in range(i)] for i in range(1,n)]
dp.append(num_list)
for i in range(n-2,-1,-1):
    for j in range(i+1):
        dp[i][j] = max(dp[i+1][j],dp[i+1][j+1])+mylist[i][j]
print(dp[0][0])