'''
Ehab loves number theory, but for some reason he hates the number x.
Given an array a, find the length of its longest subarray such that the sum of its elements isn't divisible by x, or determine that such subarray doesn't exist.
An array a is a subarray of an array b if a can be obtained from b by deletion of several (possibly, zero or all) elements from the beginning and several (possibly, zero or all) elements from the end.
Input
The first line contains an integer t(1≤𝑡≤5)— the number of test cases you need to solve. The description of the test cases follows.
The first line of each test case contains 2 integers n and x (1≤𝑛≤105, 1≤𝑥≤104) — the number of elements in the array a and the number that Ehab hates.
The second line contains n space-separated integers 𝑎1, 𝑎2, …, 𝑎𝑛(0≤𝑎𝑖≤104) — the elements of the array 𝑎
Output
For each testcase, print the length of the longest subarray whose sum isn't divisible by x. If there's no such subarray, print −1
'''

#2200015507 王一粟
k = int(input())
for p in range(k):
    num,hate = [int(i) for i in input().split()]
    elarray = [int(i) for i in input().split()]
    maximum = 0
    for inde,el in enumerate(elarray):
        if num-inde < maximum:
            break
        for i in range(num-inde-1,-1,-1):
            nowlist = elarray[inde:inde+i+1]
            if len(nowlist) < maximum:
                break
            if sum(nowlist) % hate != 0:
                maximum = len(nowlist)
                break
    if maximum == 0:
        print(-1)
    else:
        print(maximum)


def prefix_sum(nums):
    prefix = []
    total = 0
    for num in nums:
        total += num
        prefix.append(total)
    return prefix

def suffix_sum(nums):
    suffix = []
    total = 0
    reversed_nums = nums[::-1]
    for num in reversed_nums:
        total += num
        suffix.append(total)
    suffix.reverse()
    return suffix

t = int(input())
for _ in range(t):
    N, x = map(int, input().split())
    a = [int(i) for i in input().split()]
    aprefix_sum = prefix_sum(a)
    asuffix_sum = suffix_sum(a)
    left = 0
    right = N - 1
    if right == 0:
        if a[0] % x !=0:
            print(1)
        else:
            print(-1)
        continue
    leftmax = 0
    rightmax = 0
    while left != right:
        total = asuffix_sum[left]
        if total % x != 0:
            leftmax = right - left + 1
            break
        else:
            left += 1

    left = 0
    right = N - 1
    while left != right:
        total = aprefix_sum[right]
        if total % x != 0:
            rightmax = right - left + 1
            break
        else:
            right -= 1
    if leftmax == 0 and rightmax == 0:
        print(-1)
    else:
        print(max(leftmax, rightmax))