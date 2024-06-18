'''
描述
The SUM problem can be formulated as follows: given four lists A, B, C, D of integer values, compute how many quadruplet (a, b, c, d ) ∈ A x B x C x D are such that a + b + c + d = 0 . In the following, we assume that all lists have the same size n .
输入
The first line of the input file contains the size of the lists n (this value can be as large as 4000). We then have n lines containing four integer values (with absolute value as large as 228 ) that belong respectively to A, B, C and D .
输出
For each input file, your program has to write the number quadruplets whose sum is zero
'''

#2200015507 王一粟
from collections import Counter
from itertools import product
a,b,c,d = [],[],[],[]
for i in range(int(input())):
    q,w,e,r = [int(i) for i in input().split()]
    a.append(q)
    b.append(w)
    c.append(e)
    d.append(r)
ab_sum_counter = Counter(map(sum,product(a,b)))
#product函数生成一个可迭代对象，里面的元素是所有a、b两列表元素构成的元组
#sum对于这个可迭代对象里面的所有元素进行求和
#Counter对于求和得到的元素进行统计，生成的字典key表示和，value表示和统计的次数
cn = 0
for cd_sum in map(sum,product(c,d)):
    cn += ab_sum_counter.get(-cd_sum,0)
    #如果字典中有-cd_sum，则取出该key的value值，否则默认为0
print(cn)