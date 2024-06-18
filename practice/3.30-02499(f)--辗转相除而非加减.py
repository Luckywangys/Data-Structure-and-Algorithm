'''
描述
Background
Binary trees are a common data structure in computer science. In this problem we will look at an infinite binary tree where the nodes contain a pair of integers. The tree is constructed like this:
The root contains the pair (1, 1).
If a node contains (a, b) then its left child contains (a + b, b) and its right child (a, a + b)
Problem
Given the contents (a, b) of some node of the binary tree described above, suppose you are walking from the root of the tree to the given node along the shortest possible path. Can you find out how often you have to go to a left child and how often to a right child?
输入
The first line contains the number of scenarios.
Every scenario consists of a single line containing two integers i and j (1 <= i, j <= 2*109) that represent
a node (i, j). You can assume that this is a valid node in the binary tree described above.
输出
The output for every scenario begins with a line containing "Scenario #i:", where i is the number of the scenario starting at 1. Then print a single line containing two numbers l and r separated by a single space, where l is how often you have to go left and r is how often you have to go right when traversing the tree from the root to the node given in the input. Print an empty line after every scenario.
'''

#2200015507 王一粟
from functools import lru_cache
import sys
sys.setrecursionlimit(100000)
@lru_cache(maxsize=None)
def f(a,b):
    if a==1 or b==1:
        return a-1,b-1
    if a>b:
        left_num,right_num = f(a%b,b)
        return left_num+a//b,right_num
    else:
        left_num,right_num = f(a,b%a)
        return left_num, right_num + b//a
n = int(input())
for i in range(1,n+1):
    num1,num2 = [int(i) for i in input().split()]
    if i != 1:
        print()
    print(f"Scenario #{i}:")
    x,y = f(num1,num2)
    print(x,y)