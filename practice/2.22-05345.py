"""
给出N个范围在[0, 65535]的整数，编程支持以下的操作：
（1）修改操作：C d，所有的数都增加d。如果超过65535，把结果模65536。 0 <= d <= 65535
（2）查询操作：Q i，统计在N个正整数中有多少个整数其对应的二进制形式的第i位二进制位为非0。0 <= i <= 15。并且最低位i为0。
　　最后，输出所有查询操作的统计值。
输入
输入的第一行为两个正整数N,M,其中N为操作的整数的个数，而M为具体有多少个操作。
输入的第二行为N个正整数，为进行操作的N个正整数。
下面有M行，分别表示M个操作。
N<=100000,M<=200000
输出
输出所有查询操作Q的统计值，每一个查询操作统计结果输出为一行。
"""
#2200015507 王一粟
n,m = [int(k) for k in input().split()]
mylist = [int(k) for k in input().split()]
for i in range(m):
    operate,num = input().split()
    num = int(num)
    if operate == "C":
        mylist = [(k+num)%65536 for k in mylist]
    else:
        cnt = 0
        for j in mylist:
            result = j % 2**(num+1) // 2**(num)
            if result == 1:
                cnt += 1
        print(cnt)







