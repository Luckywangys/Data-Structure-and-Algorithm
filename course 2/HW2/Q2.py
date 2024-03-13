"""
描述
圣诞节来临了，在城市A中圣诞老人准备分发糖果，现在有多箱不同的糖果，每箱糖果有自己的价值和重量，每箱糖果都可以拆分成任意散装组合带走。圣诞老人的驯鹿最多只能承受一定重量的糖果，请问圣诞老人最多能带走多大价值的糖果。
输入
第一行由两个部分组成，分别为糖果箱数正整数n(1 <= n <= 100)，驯鹿能承受的最大重量正整数w（0 < w < 10000），两个数用空格隔开。其余n行每行对应一箱糖果，由两部分组成，分别为一箱糖果的价值正整数v和重量正整数w，中间用空格隔开。
输出
输出圣诞老人能带走的糖果的最大总价值，保留1位小数。输出为一行，以换行符结束。
"""

# 2200015507 王一粟
n,w = [int(i) for i in input().split()]
mydict = {}
for i in range(n):
    value,weight = [int(i) for i in input().split()]
    perprice = value/weight
    if perprice in mydict:
        mydict[perprice] = mydict[perprice] + weight
    else:
        mydict[perprice] = weight
mylist = sorted(mydict.items(),key = lambda x:x[0],reverse = True)
result = 0
weightcnt = 0
for i in mylist:
    if weightcnt + i[1] <= w:
        result = result + i[0]*i[1]
        weightcnt = weightcnt + i[1]
    else:
        result = result + i[0]*(w-weightcnt)
        break
print(round(result,1))
