'''
描述
任何一个正整数都可以用2的幂次方表示。
输入
一个正整数n（n≤20000）。
输出
一行，符合约定的n的0，2表示（在表示中不能有空格）。
'''

#2200015507
count_list = [2**i for i in range(14,-1,-1)]
def express(t):
    result = ""
    if t == 0:
        return "0"
    for index,element in enumerate(count_list):
        if element <= t:
            t = t-element
            if result == "":
                if element == 2:
                    result = result + "2"
                else:
                    result = result + "2" +"("+express(14-index)+")"
            else:
                if element == 2:
                    result = result + "+" + "2"
                else:
                    result = result + "+" + "2" +"("+express(14-index)+")"
    return result
n = int(input())
print(express(n))
