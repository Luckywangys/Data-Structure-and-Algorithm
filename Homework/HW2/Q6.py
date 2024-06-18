"""
描述
随着人工智能技术和基因编辑技术的普及，2050年的学生成绩计算与目前2018年的规则很不一样。课程成绩要求是t-prime，才是有效成绩，否则按照零分计算。
现在需要统计每位学生在一个学期中，所有有效成绩课程的平均分，需要你的帮忙。
（素数是指除了1和它本身以外,不能被任何整数整除的数。 类似地，如果整数t恰好有且仅有三个不同的正除数，我们将称为它为t-prime。）
输入
第一行位两个整数，m个学生（1≤m≤2000），n门课（1≤n≤100，每个学生选课数可以不一样）
接下来m行，每行代表学生选课获得成绩。成绩由空格分隔，成绩是整数 Xi (1≤Xi≤10^8)。
输出
共m行，每行对应一位学生有效成绩课程的平均分（小数点后保留两位）。如果该生所有选课有效成绩是零分，则输出零。
对如下样例，第一个学生所有成绩都不是t-prime，因此输出0，注意这里不保留两位小数。
第二位学生只有4分是有效分数，故输出4/3 = 1.33
第三位学生只有两门课有成绩，4和25均为t-prime，因此输出平均值14.50
"""

# 2200015507 王一粟
from math import sqrt
N = 10005
s = [True] * N
p = 2
while p*p <= N:
    if s[p]:
        for i in range(p * p, N, p):
            s[i] = False
    p += 1
m, n = [int(i) for i in input().split()]
for i in range(m):
    x = [int(i) for i in input().split()]
    sum = 0
    for num in x:
        root = int(sqrt(num))
        if num > 3 and s[root] and num == root * root:
            sum += num
    sum /= len(x)
    if sum == 0:
        print(0)
    else:
        print('%.2f' % sum)