# Assignment #1: 拉齐大家Python水平

Updated 0940 GMT+8 Feb 19, 2024

2024 spring, Complied by ==王一粟 经济学院 2200015507==



**说明：**

1）数算课程的先修课是计概，由于计概学习中可能使用了不同的编程语言，而数算课程要求Python语言，因此第一周作业练习Python编程。如果有同学坚持使用C/C++，也可以，但是建议也要会Python语言。

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）课程网站是Canvas平台, https://pku.instructure.com, 学校通知3月1日导入选课名单后启用。**作业写好后，保留在自己手中，待3月1日提交。**

提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



**编程环境**

==（请改为同学的操作系统、编程环境等）==

操作系统：macOS Ventura 13.4.1 (c)

Python编程环境：Spyder IDE 5.2.2, PyCharm 2023.1.4 (Professional Edition)

C/C++编程环境：Mac terminal vi (version 9.0.1424), g++/gcc (Apple clang version 14.0.3, clang-1403.0.22.14.1)



## 1. 题目

### 20742: 泰波拿契數

http://cs101.openjudge.cn/practice/20742/



思路：定义序列函数，内嵌迭代

耗时：10min


##### 代码

```python
# # 2200015507 王一粟
def t(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n == 0:
        return 0
    else:
        return t(n-1) + t(n-2) + t(n-3)
n = int(input())
print(t(n))

```



代码运行截图 ==（至少包含有"Accepted"）==
![1.png](1.png)

### 58A. Chat room

greedy/strings, 1000, http://codeforces.com/problemset/problem/58/A



思路：做循环，若s中存在依次排列的hello，即可判断正确

耗时：20min

##### 代码

```python
# # HW1 Q2 王一粟 2200015507
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
```



代码运行截图 ==（至少包含有"Accepted"）==
![2.png](2.png)




### 118A. String Task

implementation/strings, 1000, http://codeforces.com/problemset/problem/118/A



思路：先将字符串小写，然后对非元音字母进行顺序相加以及加入“.”

耗时：20min


##### 代码

```python
# # 2200015507 王一粟
s = input()
c = s.lower()
result = ""
for m in c:
    if m not in "yaeiou":
        result += "." + m
print(result)
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==
![3.png](3.png)




### 22359: Goldbach Conjecture

http://cs101.openjudge.cn/practice/22359/



思路：先通过函数确定判断质数的方式，然后循环找出质数&跳出即可

耗时：20min

##### 代码
```python
# # 2200015507 王一粟
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
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==
![4.png](4.png)




### 23563: 多项式时间复杂度

http://cs101.openjudge.cn/practice/23563/



思路：先将每一项进行分割，剔除系数为0的项后，运营循环方式确定最大指数

耗时：30min

##### 代码

```python
# # 2200015507 王一粟
s = input().split("+")
mylist = [i for i in s if i[0] != "0"]
result = 0
for element in mylist:
    t = element.index("^")
    cnt = int(element[t+1:])
    if cnt > result:
        result = cnt
print("n^"+str(result))
```
![5.png](5.png)


代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==





### 24684: 直播计票

http://cs101.openjudge.cn/practice/24684/



思路：字典排序输出key

耗时：20min

##### 代码

```python
# # 2200015507 王一粟
mylist = input().split()
mydict = {}
for num in mylist:
    if int(num) not in mydict:
        mydict[int(num)] = 1
    else:
        mydict[int(num)] += 1
sortdict = sorted(mydict.items(), key=lambda x: (x[1],-x[0]), reverse=True)
result = [i[0] for i in sortdict if i[1] == sortdict[0][1]]
print(" ".join(str(i) for i in result))
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==
![6.png](6.png)




## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“数算pre每日选做”、CF、LeetCode、洛谷等网站题目。==

学生非理工院系，22年选修计算概论C（100），想进一步学习计算机基础课程，故而选修数算B。编程能力较为薄弱，能感觉到 部分题目并非最优做法，且知识点遗忘程度较严重

需要进一步温习知识。如果有可能，也恳请老师/助教帮我看一下算法有哪些可以优化的地方www




