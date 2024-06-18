'''
输入
输入只有一行，包含一个整数a(0 < a < 3000)
输出
一行，如果公元a年是闰年输出Y，否则输出N
'''

#2200015507 王一粟
def istrue(n):
    if n%4 == 0:
        if n%100 == 0 and n%400 != 0:
            return "N"
        elif n%3200 == 0:
            return "N"
        else:
            return "Y"
    else:
        return "N"
a = int(input())
print(istrue(a))