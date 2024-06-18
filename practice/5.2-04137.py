'''
描述
给定一个十进制正整数n(0 < n < 1000000000)，每个数位上数字均不为0。n的位数为m。
现在从m位中删除k位(0<k < m)，求生成的新整数最小为多少？
例如: n = 9128456, k = 2, 则生成的新整数最小为12456
输入
第一行t, 表示有t组数据；
接下来t行，每一行表示一组测试数据，每组测试数据包含两个数字n, k。
输出
t行，每行一个数字，表示从n中删除k位后得到的最小整数。
'''

#2200015507 王一粟
for _ in range(int(input())):
    n,k = input().split()
    k = int(k)
    total_digit = len(n)
    num_list = [int(i) for i in str(n)]
    now_digit = 0
    result = []
    cnt = 0
    for i in range(1,total_digit-k+1):
        for j in range(now_digit,k+i):
            if num_list[j] < num_list[cnt]:
                cnt = j
        now_digit = cnt + 1
        result.append(num_list[cnt])
        cnt = cnt + 1
    print("".join(str(i) for i in result))