'''
描述
Given three strings, you are to determine whether the third string can be formed by combining the characters in the first two strings. The first two strings can be mixed arbitrarily, but each must stay in its original order.
For example, consider forming "tcraete" from "cat" and "tree":
String A: cat
String B: tree
String C: tcraete
As you can see, we can form the third string by alternating characters from the two strings. As a second example, consider forming "catrtee" from "cat" and "tree":
String A: cat
String B: tree
String C: catrtee
Finally, notice that it is impossible to form "cttaree" from "cat" and "tree".
输入
The first line of input contains a single positive integer from 1 through 1000. It represents the number of data sets to follow. The processing for each data set is identical. The data sets appear on the following lines, one data set per line.
For each data set, the line of input consists of three strings, separated by a single space. All strings are composed of upper and lower case letters only. The length of the third string is always the sum of the lengths of the first two strings. The first two strings will have lengths between 1 and 200 characters, inclusive.
输出
For each data set, print:
Data set n: yes
if the third string can be formed from the first two, or
Data set n: no
if it cannot. Of course n should be replaced by the data set number. See the sample output below for an example.
'''

#2200015507 王一粟
#函数内想要修改全局变量的值，用global。调用无需global

def dfs(x,y):
    if x == -1 and y==-1:
        return True
    if x>=0:
        if y>=0:
            if a[x] == c[x+y+1]:
                if dfs(x-1,y):return True
            if b[y] == c[x+y+1]:
                if dfs(x,y-1):return True
        else:
            if a[:x+1] == c[:x+1]:return True
    else:
        if b[:y+1] == c[:y+1]:return True
    return False
n = int(input())
for i in range(1,n+1):
    a,b,c = input().split()
    length1 = len(a)
    length2 = len(b)
    if dfs(len(a)-1,len(b)-1):
        print(f"Data set {i}: yes")
    else:
        print(f"Data set {i}: no")