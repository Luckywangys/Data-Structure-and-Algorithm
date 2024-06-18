'''
描述
Paul是一名数学专业的同学，在课余选修了C++编程课，现在他能够自己写程序判断判断一个给定的由'('和')'组成的字符串是否是正确匹配的。可是他不满足于此，想反其道而行之，设计一个程序，能够生成所有合法的括号组合，请你帮助他解决这个问题。
输入
输入只有一行N，代表生成括号的对数（1 ≤ N ≤ 10)。
输出
输出所有可能的并且有效的括号组合，按照字典序进行排列，每个组合占一行。
'''

#2200015507 王一粟
n = int(input())
candidate = [["("]]
operate = []
for _ in range(2*n-1):
    for candidate_element in candidate:
        left_cnt = candidate_element.count("(")
        right_cnt = len(candidate_element) - left_cnt
        if left_cnt < n:
            operate.append(candidate_element+["("])
        if left_cnt > right_cnt:
            operate.append(candidate_element+[")"])
    candidate = operate
    operate = []
result = sorted(candidate)
for mylist in result:
    print("".join(mylist))