'''
给出一系列非负整数，判断是否是一个回文数。回文数指的是正着写和倒着写相等的数。
输入
若干行，每行是一个非负整数（不超过99999999）
输出
对每行输入，如果其是一个回文数，输出YES。否则输出NO。
'''

#2200015507 王一粟
while True:
    try:
        s = input()
        sreverse = int(s[::-1])
        sright = int(s)
        if sreverse == sright:
            print("YES")
        else:
            print("NO")
    except:
        break