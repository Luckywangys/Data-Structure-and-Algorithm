'''
描述
约瑟夫问题：有ｎ只猴子，按顺时针方向围成一圈选大王（编号从１到ｎ），从第１号开始报数，一直数到ｍ，数到ｍ的猴子退出圈外，剩下的猴子再接着从1开始报数。就这样，直到圈内只剩下一只猴子时，这个猴子就是猴王，编程求输入ｎ，ｍ后，输出最后猴王的编号。
输入
每行是用空格分开的两个整数，第一个是 n, 第二个是 m ( 0 < m,n <=300)。最后一行是：
0 0
输出
对于每行输入数据（最后一行除外)，输出数据也是一行，即最后猴王的编号
'''

#2200015507 王一粟
while True:
    n, m = [int(i) for i in input().split()]
    if n == 0 and m==0:
        break
    mylist = [int(i) for i in range(1, n + 1)]
    cnt = 0
    while len(mylist) > 1:
        t = len(mylist)
        del mylist[(cnt+m - 1)%t]
        cnt = (cnt+m-1)%t
    print(mylist[0])

