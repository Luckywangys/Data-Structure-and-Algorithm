'''
Q4
Given the sum of prime A and prime B, find A and B.
'''

# 2200015507 王一粟
def isprime(n):
    if n == 2:
        return True
    else:
        cnt = 0
        for i in range(2,n):
            if n % i == 0:
                cnt = 1
                break
        if cnt == 1:
            return False
        else:
            return True
n = int(input())
for m in range(2,int(n/2)+1):
    if isprime(m) and isprime(n-m):
        print(m,n-m)
        break

#思路：先通过函数确定判断质数的方式，然后循环找出质数&跳出即可
#耗时：20min