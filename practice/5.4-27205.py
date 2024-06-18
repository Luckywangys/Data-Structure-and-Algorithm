'''
描述
在一片保护林中，护林员想要盖一座房子来居住，但他不能砍伐任何树木。 现在请你帮他计算：保护林中所能用来盖房子的矩形空地的最大面积。
输入
保护林用一个二维矩阵来表示，长宽都不超过1000（即<=1000）。
第一行是两个正整数m,n，表示矩阵有m行n列。
然后是m行，每行n个整数，用1代表树木，用0表示空地。
输出
一个正整数，表示保护林中能用来盖房子的最大矩形空地面积。
'''

#2200015507 王一粟
def solution(mylist,n):
    stack = []
    result = [0 for i in range(n)]
    for idx,element in enumerate(mylist):
        while stack and element < mylist[stack[-1]]:
            a = stack.pop()
            if stack:
                result[a] += idx-stack[-1]-1
            else:
                result[a] += idx-a
        stack.append(idx)
    prev = stack[0]
    result[stack[0]] = n
    for element in stack[1:]:
        if mylist[element] == mylist[prev]:
            result[element] = result[prev]
        else:
            result[element] = n - prev - 1
        prev = element
    return result
m,n = [int(i) for i in input().split()]
total = 0
mylist = [0 for i in range(n)]
for i in range(1,m+1):
    s = [int(i) for i in input().split()]
    for idx,element in enumerate(s):
        if element == 0:
            mylist[idx] += 1
        else:
            mylist[idx] = 0
    process = solution(mylist,n)
    for idx,element in enumerate(process):
        total = max(element*mylist[idx],total)
print(total)


