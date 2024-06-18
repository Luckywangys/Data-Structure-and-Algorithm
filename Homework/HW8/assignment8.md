# Assignment #8: 图论：概念、遍历，及 树算

Updated 1150 GMT+8 Apr 8, 2024

2024 spring, Complied by ==同学的姓名、院系==



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



**编程环境**

==（请改为同学的操作系统、编程环境等）==

操作系统：macOS Ventura 13.4.1 (c)

Python编程环境：Spyder IDE 5.2.2, PyCharm 2023.1.4 (Professional Edition)

C/C++编程环境：Mac terminal vi (version 9.0.1424), g++/gcc (Apple clang version 14.0.3, clang-1403.0.22.14.1)



## 1. 题目

### 19943: 图的拉普拉斯矩阵

matrices, http://cs101.openjudge.cn/practice/19943/



思路：



代码

```python
#2200015507 王一粟
n,m = [int(i) for i in input().split()]
edges = [[0]*n for i in range(n)]
for _ in range(m):
    v1,v2 = [int(i) for i in input().split()]
    edges[v1][v1] += 1
    edges[v2][v2] += 1
    edges[v1][v2] -= 1
    edges[v2][v1] -= 1
for _ in range(n):
    print(" ".join(str(i) for i in edges[_]))
```



代码运行截图 ==（至少包含有"Accepted"）==





### 18160: 最大连通域面积

matrix/dfs similar, http://cs101.openjudge.cn/practice/18160



思路：



代码

```python
#2200015507 王一粟
def dfs(i,j,n,m):
    graph[i][j] = "."
    result = 1
    for di,dj in [(1,0),(0,1),(-1,0),(0,-1),(-1,-1),(1,1),(-1,1),(1,-1)]:
        if 0<=i+di<n and 0<=j+dj<m and graph[i+di][j+dj] == "W":
            result += dfs(i+di,j+dj,n,m)
    return result
t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    graph = []
    for i in range(n):
        graph.append(list(input()))
    max_result = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == "W":
                t = dfs(i,j,n,m)
                if t > max_result:
                    max_result = t
    print(max_result)
```



代码运行截图 ==（至少包含有"Accepted"）==





### sy383: 最大权值连通块


思路：



代码

```python
#2200015507 王一粟
def dfs(i):
    visited[i] = 1
    result = weight[i]
    for j in graph[i]:
        if visited[j] == 0:
            result += dfs(j)
    return result
n,m = [int(i) for i in input().split()]
weight = [int(i) for i in input().split()]
graph = {i: [] for i in range(n)}
visited = [0]*n
for _ in range(m):
    key1,key2 = [int(i) for i in input().split()]
    graph[key1].append(key2)
    graph[key2].append(key1)
max_result = 0
for i in range(n):
    if visited[i] == 0:
        t = dfs(i)
        if t > max_result:
            max_result = t
print(max_result)
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==





### 03441: 4 Values whose Sum is 0

data structure/binary search, http://cs101.openjudge.cn/practice/03441



思路：



代码

```python
#2200015507 王一粟
from collections import Counter
from itertools import product
a,b,c,d = [],[],[],[]
for i in range(int(input())):
    q,w,e,r = [int(i) for i in input().split()]
    a.append(q)
    b.append(w)
    c.append(e)
    d.append(r)
ab_sum_counter = Counter(map(sum,product(a,b)))
#product函数生成一个可迭代对象，里面的元素是所有a、b两列表元素构成的元组
#sum对于这个可迭代对象里面的所有元素进行求和
#Counter对于求和得到的元素进行统计，生成的字典key表示和，value表示和统计的次数
cn = 0
for cd_sum in map(sum,product(c,d)):
    cn += ab_sum_counter.get(-cd_sum,0)
    #如果字典中有-cd_sum，则取出该key的value值，否则默认为0
print(cn) 

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==





### 04089: 电话号码

trie, http://cs101.openjudge.cn/practice/04089/



思路：



代码

```python
#2200015507 王一粟
class TrieNode:
    def __init__(self):
        self.child = [None]*10
        self.wordCount = 0
for _ in range(int(input())):
    n = int(input())
    root = TrieNode()
    cnt = 0
    for i in range(n):
        s = input()
        current_node = root
        for idx,element in enumerate(s):
            if cnt == 1:
                break
            if current_node.child[int(element)] is None:
                new_node = TrieNode()
                current_node.child[int(element)] = new_node
                current_node = new_node
            else:
                if current_node.child[int(element)].wordCount != 0:
                    cnt = 1
                    break
                else:
                    current_node = current_node.child[int(element)]
                    if idx == len(s)-1:
                        cnt = 1
            if idx == len(s)-1:
                current_node.wordCount = 1
    if cnt == 1:
        print("NO")
    else:
        print("YES")
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==





### 04082: 树的镜面映射

http://cs101.openjudge.cn/practice/04082/



思路：



代码

```python
#2200015507 王一粟
from collections import deque
class Node:
    def __init__(self,val):
        self.val = val
        self.child = deque()
        self.parent = None
    def get(self):
        return self.val

n = int(input())
s = input().split()
root = Node(s[0][0])
stack = [[root,0]]
for i in s[1:]:
    value = i[0]
    property = int(i[1])
    if value != "$":
        current_node = Node(value)
        if stack[-1][-1] == 0:
            current_node.parent = stack[-1][0]
            stack[-1][0].child.appendleft(current_node)
            stack[-1][1] = 1
            if property == 0:
                stack.append([current_node,0])
        else:
            current_node.parent = stack[-1][0].parent
            stack[-1][0].parent.child.appendleft(current_node)
            stack.pop()
            if property == 0:
                stack.append([current_node,0])
    else:
        if stack[-1][-1] == 0:
            stack[-1][-1] = 1
        else:
            stack.pop()
queue = deque([root])
result = []
while queue:
    node = queue.popleft()
    result.append(node.get())
    queue.extend(node.child)
print(" ".join(result))
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==





## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“2024spring每日选做”、CF、LeetCode、洛谷等网站题目。==





