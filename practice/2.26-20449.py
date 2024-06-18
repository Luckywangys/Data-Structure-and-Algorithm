'''
描述
给定由0 和 1 组成的字串 A，我们定义 N_i：从 A[0] 到 A[i] 的第 i 个子数组被解释为一个二进制数
返回0和 1 组成的字串 answer，只有当 N_i 可以被 5 整除时，答案 answer[i] 为 1，否则为 0
输入
一个0和1组成的字串
输出
一行长度等同于输入的0和1组成的字串
'''

#2200015507 王一粟
def binary(s):
    astring = s[::-1]
    cnt = 0
    result = 0
    for i in astring:
        num = int(i)
        result = result + num*(2**(cnt))
        cnt = cnt + 1
    return result
def isdivisible(n):
    if n%5 == 0:
        return 1
    else:
        return 0
mylist = []
s = input()
for i in range(len(s)):
    subs = s[0:i+1]
    result = binary(subs)
    outresult = isdivisible(result)
    mylist.append(outresult)
print("".join(str(i) for i in mylist))

