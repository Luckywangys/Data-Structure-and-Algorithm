'''
描述
很久很久以前，森林里住着一群兔子。兔子们无聊的时候就喜欢研究星座。如图所示，天空中已经有了n颗星星，其中有些星星有边相连。兔子们希望删除掉一些边，然后使得保留下的边仍能是n颗星星连通。他们希望计算，保留的边的权值之和最小是多少？
输入
第一行只包含一个表示星星个数的数n，n不大于26，并且这n个星星是由大写字母表里的前n个字母表示。接下来的n-1行是由字母表的前n-1个字母开头。最后一个星星表示的字母不用输入。对于每一行，以每个星星表示的字母开头，然后后面跟着一个数字，表示有多少条边可以从这个星星到后面字母表中的星星。如果k是大于0，表示该行后面会表示k条边的k个数据。每条边的数据是由表示连接到另一端星星的字母和该边的权值组成。权值是正整数的并且小于100。该行的所有数据字段分隔单一空白。该星星网络将始终连接所有的星星。该星星网络将永远不会超过75条边。没有任何一个星星会有超过15条的边连接到其他星星（之前或之后的字母）。在下面的示例输入，数据是与上面的图相一致的。
输出
输出是一个整数，表示最小的权值和
'''

#2200015507 王一粟
import heapq
n = int(input())
graph = {chr(65+i):{} for i in range(n)}
for _ in range(n-1):
    s = input().split()
    key = s[0]
    num = int(s[1])
    for i in range(num):
        graph[key][s[i*2+2]] = int(s[i*2+3])
        graph[s[i*2+2]][key] = int(s[i*2+3])
visited = ["A"]
mylist = [(value,"A",key_to) for key_to,value in graph["A"].items()]
weight = 0
heapq.heapify(mylist)
while mylist:
    distance,fro,to = heapq.heappop(mylist)
    if to not in visited:
        visited.append(to)
        weight += distance
        for next_to,next_distance in graph[to].items():
            if next_to not in visited:
                heapq.heappush(mylist,(next_distance,to,next_to))
print(weight)










