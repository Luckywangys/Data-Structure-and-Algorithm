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
result = ""
num_list = [int(i) for i in list(input())]
num = 0
for element in num_list:
    num = num*2 + element
    if num%5 == 0:
        result += str(1)
    else:
        result += str(0)
print(result)