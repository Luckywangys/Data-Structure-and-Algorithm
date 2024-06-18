'''
描述
很久很久之前，森林里住着一群兔子。有一天，兔子们希望去赏樱花，但当他们到了上野公园门口却忘记了带地图。现在兔子们想求助于你来帮他们找到公园里的最短路。
输入
输入分为三个部分。
第一个部分有P+1行（P<30），第一行为一个整数P，之后的P行表示上野公园的地点, 字符串长度不超过20。
第二个部分有Q+1行（Q<50），第一行为一个整数Q，之后的Q行每行分别为两个字符串与一个整数，表示这两点有直线的道路，并显示二者之间的矩离（单位为米）。
第三个部分有R+1行（R<20），第一行为一个整数R，之后的R行每行为两个字符串，表示需要求的路线。
输出
输出有R行，分别表示每个路线最短的走法。其中两个点之间，用->(矩离)->相隔。
'''

#2200015507 王一粟
class Node:
    def __init__(self,val):
        self.val = val
        self.prev = None
import heapq
p = int(input())
graph = {}
for i in range(p):
    spot = input()
    graph[spot] = {}
q = int(input())
for i in range(q):
    spot1,spot2,distance = input().split()
    dis = int(distance)
    graph[spot1][spot2] = dis
    graph[spot2][spot1] = dis
r = int(input())
for i in range(r):
    start,end = input().split()
    if start == end:
        print(start)
        continue
    distance = {start:0}
    node_dict = {start:Node(start)}
    mylist = []
    heapq.heappush(mylist,[0,start])
    while mylist:
        dist,spot = heapq.heappop(mylist)
        if distance[spot] != dist:
            continue
        distance[spot] = dist
        if spot == end:
            result = end
            current_node = end
            while True:
                if current_node == start:
                    print(result)
                    break
                past_node = node_dict[current_node].prev
                result = past_node + "->(" +str(graph[past_node][current_node]) + ")->" + result
                current_node = past_node
            break
        for neighbor,inter_dis in graph[spot].items():
            if neighbor in distance and distance[neighbor] < dist+inter_dis:
                continue
            heapq.heappush(mylist,[dist+inter_dis,neighbor])
            distance[neighbor] = dist+inter_dis
            if neighbor not in node_dict:
                new_node = Node(neighbor)
                new_node.prev = spot
                node_dict[neighbor] = new_node
            else:
                node_dict[neighbor].prev = spot