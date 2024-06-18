'''
描述
输入一个正整数N。把N拆成若干个(至少一个)两两不同的正奇数的和，请问有多少种拆分方法？
输入
一个正整数N。(1 <= N <= 100)
输出
先按字典序输出所有的拆分方案，每个方案一行。
最后一行输出方案总数
'''

#2200015507 王一粟
def dfs(i,k,wait_answer):
    if k == 0:
        result.append(wait_answer)
        return
    for j in range(i,k+1,2):
        dfs(j+2,k-j,wait_answer+[j])
n = int(input())
result = []
dfs(1,n,[])
cnt = 0
for element in result:
    print(" ".join(str(i) for i in element))
    cnt += 1
print(cnt)


