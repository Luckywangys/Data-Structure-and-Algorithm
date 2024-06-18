'''
描述
给你一些电话号码，请判断它们是否是一致的，即是否有某个电话是另一个电话的前缀。比如：
Emergency 911
Alice 97 625 999
Bob 91 12 54 26
在这个例子中，我们不可能拨通Bob的电话，因为Emergency的电话是它的前缀，当拨打Bob的电话时会先接通Emergency，所以这些电话号码不是一致的。
输入
第一行是一个整数t，1 ≤ t ≤ 40，表示测试数据的数目。
每个测试样例的第一行是一个整数n，1 ≤ n ≤ 10000，其后n行每行是一个不超过10位的电话号码。
输出
对于每个测试数据，如果是一致的输出“YES”，如果不是输出“NO”。
'''

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