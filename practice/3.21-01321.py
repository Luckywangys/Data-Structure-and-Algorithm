'''
描述
在一个给定形状的棋盘（形状可能是不规则的）上面摆放棋子，棋子没有区别。要求摆放时任意的两个棋子不能放在棋盘中的同一行或者同一列，请编程求解对于给定形状和大小的棋盘，摆放k个棋子的所有可行的摆放方案C。
输入
输入含有多组测试数据。
每组数据的第一行是两个正整数，n k，用一个空格隔开，表示了将在一个n*n的矩阵内描述棋盘，以及摆放棋子的数目。 n <= 8 , k <= n
当为-1 -1时表示输入结束。
随后的n行描述了棋盘的形状：每行有n个字符，其中 # 表示棋盘区域， . 表示空白区域（数据保证不出现多余的空白行或者空白列）。
输出
对于每一组数据，给出一行输出，输出摆放的方案数目C （数据保证C<2^31）
'''

#2200015507
ans = 0
def traceback(row,wait_list,n,arranged,k):
    global ans
    if row == n+1:
        if arranged == k:
            ans += 1
    elif arranged == k:
        ans += 1
    else:
        if arranged + n -row + 1 >= k:
            for element in space_list[row]:
                if element not in wait_list:
                    wait_list.append(element)
                    traceback(row + 1, wait_list, n,arranged+1,k)
                    wait_list.pop()
            traceback(row + 1, wait_list,n,arranged,k)

while True:
    n,k = [int(i) for i in input().split()]
    if n == -1:
        break
    space_list = [0]
    for i in range(1,n+1):
        s = input()
        mylist = [i+1 for i in range(n) if s[i] == "#"]
        space_list.append(mylist)
    ans = 0
    traceback(1,[],n,0,k)
    print(ans)