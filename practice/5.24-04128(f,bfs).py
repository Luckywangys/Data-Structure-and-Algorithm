'''
描述
给出两个单词（开始单词和结束单词）以及一个词典。找出从开始单词转换到结束单词，所需要的最短转换序列。转换的规则如下：
1、每次只能改变一个字母
2、转换过程中出现的单词(除开始单词和结束单词)必须存在于词典中
例如：
开始单词为：hit
结束单词为：cog
词典为：[hot,dot,dog,lot,log,mot]
那么一种可能的最短变换是： hit -> hot -> dot -> dog -> cog,
所以返回的结果是序列的长度5；
注意：
1、如果不能找到这种变换，则输出0；
2、词典中所有单词长度一样；
3、所有的单词都由小写字母构成；
4、开始单词和结束单词可以不在词典中。
输入
共两行，第一行为开始单词和结束单词（两个单词不同），以空格分开。第二行为若干的单词（各不相同），以空格分隔开来，表示词典。单词长度不超过5,单词个数不超过30。
输出
输出转换序列的长度。
'''

#2200015507 王一粟
from collections import deque
start,end = input().split()
mylist = input().split() + [start,end]
n = len(mylist[0])
if len(start) != n:
    print(0)
    exit()
bucket = {}
for element in mylist:
    for i in range(n):
        x = element[:i] + "_" + element[i+1:]
        if x in bucket:
            bucket[x].add(element)
        else:
            bucket[x] = {element}
graph = {}
for similar_words in bucket.values():
    for word1 in similar_words:
        for word2 in similar_words - {word1}:
            if word1 not in graph:
                graph[word1] = [word2]
            else:
                graph[word1].append(word2)
if start not in graph or end not in graph:
    print(0)
    exit()
visited = set()
queue = deque([(start,1)])
cnt = 0
while queue:
    node,num = queue.popleft()
    for neighbor in graph[node]:
        if neighbor in visited:
            continue
        visited.add(neighbor)
        if neighbor == end:
            cnt = 1
            print(num+1)
            exit()
        queue.append((neighbor,num+1))
if cnt == 0:
    print(0)

















