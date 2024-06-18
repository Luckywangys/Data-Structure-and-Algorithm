"""
Q2
Input
The first and only line contains the word s, which Vasya typed.
This word consists of small Latin letters,
its length is no less that 1 and no more than 100 letters.
Output
If Vasya managed to say hello, print "YES", otherwise print "NO".
"""

# HW1 Q2 王一粟 2200015507
s = input()
cnt = 0
for i in s:
    if cnt == 0:
        if i == "h":
            cnt = 1
    elif cnt == 1:
        if i == "e":
            cnt = 2
    elif cnt == 2:
        if i == "l":
            cnt = 3
    elif cnt == 3:
        if i == "l":
            cnt = 4
    else:
        if i == "o":
            cnt = 5
            break
if cnt == 5:
    print("YES")
else:
    print("NO")

# 思路：做循环，若s中存在依次排列的hello，即可判断正确
# 耗时：20min
