'''
描述
Given a positive integer n, write a program to find out a nonzero multiple m of n whose decimal representation contains only the digits 0 and 1. You may assume that n is not greater than 200 and there is a corresponding m containing no more than 100 decimal digits.
输入
The input file may contain multiple test cases. Each line contains a value of n (1 <= n <= 200). A line containing a zero terminates the input.
输出
For each value of n in the input print a line containing the corresponding value of m. The decimal representation of m must not contain more than 100 digits. If there are multiple solutions for a given value of n, any one of them is acceptable.
'''

#2200015507 王一粟
from collections import deque
def find(n):
    if n == 1:
        return 1
    queue = deque([10,11])
    mylist = [1]
    while queue:
        element = queue.popleft()
        t = element % n
        if t == 0:
            return str(element)
        else:
            if t not in mylist:
                mylist.append(t)
                queue.append(element*10+1)
                queue.append(element*10)
while True:
    n = int(input())
    if n == 0:
        break
    else:
        print(find(n))

