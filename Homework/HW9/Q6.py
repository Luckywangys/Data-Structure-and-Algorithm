'''
描述
在一个国际象棋棋盘上，一个棋子“马”（骑士），按照“马走日”的规则，从一个格子出发，要走遍所有棋盘格恰好一次。把一个这样的走棋序列称为一次“周游“。在 8 × 8 的国际象棋棋盘上，合格的“周游”数量有 1.305×10^35这么多，走棋过程中失败的周游就更多了。
采用图搜索算法，是解决骑士周游问题最容易理解和编程的方案之一，解决方案分为两步： 首先用图表示骑士在棋盘上的合理走法； 采用图搜索算法搜寻一个长度为（行 × 列-1）的路径，路径上包含每个顶点恰一次。
输入
两行。
第一行是一个整数n，表示正方形棋盘边长，3 <= n <= 19。
第二行是空格分隔的两个整数sr, sc，表示骑士的起始位置坐标。棋盘左上角坐标是 0 0。0 <= sr <= n-1, 0 <= sc <= n-1。
输出
如果是合格的周游，输出 success，否则输出 fail。
'''
#2200015507 王一粟
class Vertex:
    def __init__(self,key):
        self.key = key
        self.neighbors = []
        self.color = "white"
    def add_neighbor(self,key2):
        return self.neighbors.append(key2)
class Graph:
    def __init__(self):
        self.vertices = {}
    def add_edges(self,key1,key2):
        if key1 not in self.vertices:
            self.vertices[key1] = Vertex(key1)
        if key2 not in self.vertices:
            self.vertices[key2] = Vertex(key2)
        self.vertices[key1].add_neighbor(key2)
def valid_pos(a,b,n):
    result = []
    for dx,dy in [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]:
        if 0<=a+dx<n and 0<=b+dy<n:
            result.append([a+dx,b+dy])
    return result
def order(key):
    mylist = mygraph.vertices[key].neighbors
    operate = []
    for element_key in mylist:
        current_node = mygraph.vertices[element_key]
        if current_node.color == "white":
            c = 0
            for w in current_node.neighbors:
                if mygraph.vertices[w].color == "white":
                    c+=1
            operate.append([element_key,c])
    operate.sort(key = lambda x:x[1])
    return [x[0] for x in operate]
def dfs(x,y,t,n):
    mygraph.vertices[(x,y)].color = "grey"
    if t == n**2:
        return True
    for node in order((x,y)):
        if dfs(node[0],node[1],t+1,n):
            return True
    mygraph.vertices[(x,y)].color = "white"
    return False
n = int(input())
sr,sc = [int(i) for i in input().split()]
mygraph = Graph()
for i in range(n):
    for j in range(n):
        legal_id = valid_pos(i,j,n)
        for p,q in legal_id:
            mygraph.add_edges((i,j),(p,q))
if dfs(sr,sc,1,n):
    print("success")
else:
    print("fail")