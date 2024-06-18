'''
描述
词梯问题是由“爱丽丝漫游奇境”的作者 Lewis Carroll 在1878年所发明的单词游戏。从一个单词演变到另一个单词，其中的过程可以经过多个中间单词。要求是相邻两个单词之间差异只能是1个字母，如fool -> pool -> poll -> pole -> pale -> sale -> sage。与“最小编辑距离”问题的区别是，中间状态必须是单词。目标是找到最短的单词变换序列。
假设有一个大的单词集合（或者全是大写单词，或者全是小写单词），集合中每个元素都是四个字母的单词。采用图来解决这个问题，如果两个单词的区别仅在于有一个不同的字母，就用一条边将它们相连。如果能创建这样一个图，那么其中的任意一条连接两个单词的路径就是词梯问题的一个解，我们要找最短路径的解。下图展示了一个小型图，可用于解决从 fool 到sage的词梯问题。
注意，它是无向图，并且边没有权重。
输入
输入第一行是个正整数 n，表示接下来有n个四字母的单词，每个单词一行。2 <= n <= 4000。
随后是 1 行，描述了一组要找词梯的起始单词和结束单词，空格隔开。
输出
输出词梯对应的单词路径，空格隔开。如果不存在输出 NO。
如果有路径，保证有唯一解。
'''

#2200015507 王一粟
from collections import deque
class Vertex:
    def __init__(self,value):
        self.value = value
        self.neighbors = []
        self.previous = None
        self.color = "white"
    def get_word(self):
        return self.value
    def get_neighbors(self):
        return self.neighbors
    def add_neighbor(self,tword):
        self.neighbors.append(tword)
class Graph:
    def __init__(self):
        self.vertices = {}
    def add_edge(self,word1,word2):
        if word1 not in self.vertices:
            self.vertices[word1] = Vertex(word1)
        if word2 not in self.vertices:
            self.vertices[word2] = Vertex(word2)
        self.vertices[word1].add_neighbor(self.vertices[word2])
    def get(self,word):
        if word in self.vertices:
            return self.vertices[word]
        else:
            a = Vertex(word)
            self.vertices[word] = a
            return a
def build_graph(all_words):
    buckets = {}
    the_graph = Graph()
    for word in all_words:
        for i,char in enumerate(word):
            bucket = word[:i]+"_"+word[i+1:]
            buckets.setdefault(bucket,set()).add(word)
    for similar_words in buckets.values():
            for word1 in similar_words:
                for word2 in similar_words-{word1}:
                    the_graph.add_edge(word1,word2)
    return the_graph
def bfs(start_word):
    myqueue = deque([start_word])
    while myqueue:
        current_word = myqueue.popleft()
        for neighbor in current_word.get_neighbors():
            if neighbor.color == "white":
                neighbor.color = "gray"
                neighbor.previous = current_word
                myqueue.append(neighbor)
        current_word.color = "black"
def traceback(the_word):
    result = [the_word.get_word()]
    if the_word.previous is not None:
        result.extend(traceback(the_word.previous))
    return result
n = int(input())
all_words = []
for _ in range(n):
    all_words.append(input())
mygraph = build_graph(all_words)


start,end = input().split()
bfs(mygraph.get(start))
re = traceback(mygraph.get(end))
if re[-1] == start:
    print(" ".join(re[::-1]))
else:
    print("NO")
