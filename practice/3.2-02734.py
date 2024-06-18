'''
描述
把一个十进制正整数转化成八进制。
输入
一行，仅含一个十进制表示的整数a(0 < a < 65536)。
输出
一行，a的八进制表示。
'''

#2200015507 王一粟
a = int(input())
result = ""
while True:
    if a <=7:
        result = str(a)+result
        break
    else:
        m = a%8
        result = str(m) + result
        a = a//8
print(result)