'''
We know that prime numbers are positive integers that have exactly two distinct positive divisors. Similarly, we'll call a positive integer t Т-prime, if t has exactly three distinct positive divisors.
You are given an array of n positive integers. For each of them determine whether it is Т-prime or not.
Input
The first line contains a single positive integer, n, showing how many numbers are in the array. The next line contains n space-separated integers xi.
Please, do not use the %lld specifier to read or write 64-bit integers in С++. It is advised to use the cin, cout streams or the %I64d specifier.
Output
Print n lines: the i-th line should contain "YES" (without the quotes), if number xi is Т-prime, and "NO" (without the quotes), if it isn't.
'''

#2200015507 王一粟
primelist = [True]*(10**6+1)
primelist[0] = False
primelist[1] = False
p = 2
while p*p <= 10**6:
    if primelist[p]:
        for i in range(p*p,10**6+1,p):
            primelist[i] = False
    p = p + 1
n = int(input())
mylist = [int(i) for i in input().split()]
for num in mylist:
    if num**0.5 == int(num**0.5) and primelist[int(num**0.5)]:
        print("YES")
    else:
        print("NO")
