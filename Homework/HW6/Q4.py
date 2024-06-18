'''
描述
根据字符使用频率(权值)生成一棵唯一的哈夫曼编码树。生成树时需要遵循以下规则以确保唯一性：
选取最小的两个节点合并时，节点比大小的规则是:
1) 权值小的节点算小。权值相同的两个节点，字符集里最小字符小的，算小。
例如 （{'c','k'},12) 和 ({'b','z'},12)，后者小。
2) 合并两个节点时，小的节点必须作为左子节点
3) 连接左子节点的边代表0,连接右子节点的边代表1
然后对输入的串进行编码或解码
输入
第一行是整数n，表示字符集有n个字符。
接下来n行，每行是一个字符及其使用频率（权重）。字符都是英文字母。
再接下来是若干行，有的是字母串，有的是01编码串。
输出
对输入中的字母串，输出该字符串的编码
对输入中的01串,将其解码，输出原始字符串
'''

#2200015507 王一粟
import heapq
class Node:
    def __init__(self,val):
        self.value = val
        self.char = None
        self.left = None
        self.right = None
    def __lt__(self,other):
        if self.value == other.value:
            return ord(self.char) < ord(self.char)
        return self.value < other.value
    def get_value(self):
        return self.value
    def get_char(self):
        return self.char

def decode(ini_root,wait_string):
    now_node = ini_root
    result = ""
    for char in wait_string:
        if char == "1":
            now_node = now_node.right
        else:
            now_node = now_node.left
        if now_node.left is None:
            result += now_node.get_char()
            now_node = ini_root
    return result
def encode(ini_root):
    codes = {}
    def parse(node,code):
        if node.left is None:
            codes[node.get_char()] = code
        else:
            parse(node.left,code+"0")
            parse(node.right,code+"1")
    parse(ini_root,"")
    return codes
n = int(input())
mylist = []
for _ in range(n):
    word,freq = input().split()
    freq = int(freq)
    current_node = Node(freq)
    current_node.char = word
    mylist.append(current_node)
heapq.heapify(mylist)
for i in range(len(mylist)-1):
    small = heapq.heappop(mylist)
    big = heapq.heappop(mylist)
    add_node = Node(small.get_value()+big.get_value())
    if ord(small.get_char()) < ord(big.get_char()):
        add_node.char = small.get_char()
    else:
        add_node.char = big.get_char()
    add_node.left = small
    add_node.right = big
    heapq.heappush(mylist,add_node)
root = mylist[0]
code_dict = encode(root)
while True:
    try:
        s = input()
        if s[0] == "0" or s[0] == "1":
            print(decode(root,s))
        else:
            ex = ""
            for element in s:
                ex += code_dict[element]
            print(ex)
    except:
        break