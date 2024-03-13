"""
输入
空格分割的一行字符串。第一个分数的分子 第一个分数的分母 第二个分数的分子 第二个分数的分母
输出
输出相加的结果。使用标准的斜线形式来显示分数，并且要求是最简分数。
"""

#2200015507 王一粟
def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm % oldn
    return n
class fraction:
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom

    def show(self):
        print(str(self.num)+"/"+str(self.den))

    def __add__(self,other):
        newnum = self.num*other.den + other.num*self.den
        newden = self.den * other.den
        common = gcd(newnum,newden)
        return fraction(newnum//common,newden//common)

m = input().split()
resultlist = [int(i) for i in m]
#(fraction(resultlist[0], resultlist[1]) + fraction(resultlist[2], resultlist[3])).show()
fraction.show(fraction(resultlist[0], resultlist[1]) + fraction(resultlist[2], resultlist[3]))