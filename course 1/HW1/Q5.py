'''
Q4
输入
一行，一个字符串表示此算法的整体运算次数，保证每项形如 x^b 或 ax^b，其中a、b均为非负整数；保证项与项之间以+号连接，保证至少存在一项。保证a, b <= 10^8
输出
一行，一个字符串 n^k 表示此算法的渐进时间复杂度为 O(n^k).
'''

# 2200015507 王一粟
s = input().split("+")
mylist = [i for i in s if i[0] != "0"]
result = 0
for element in mylist:
    t = element.index("^")
    cnt = int(element[t+1:])
    if cnt > result:
        result = cnt
print("n^"+str(result))

#思路：先将每一项进行分割，剔除系数为0的项后，运用循环方式确定最大指数
#耗时：30min