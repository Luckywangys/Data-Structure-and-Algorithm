'''
输入
你的任务是写一个程序读取一些测试数据。每组测试数据表示一个计算机的文件结构。每组测试数据以'*'结尾，而所有合理的输入数据以'#'结尾。一组测试数据包括一些文件和目录的名字（虽然在输入中我们没有给出，但是我们总假设ROOT目录是最外层的目录）。在输入中,以']'表示一个目录的内容的结束。目录名字的第一个字母是'd'，文件名字的第一个字母是'f'。文件名可能有扩展名也可能没有（比如fmyfile.dat和fmyfile）。文件和目录的名字中都不包括空格,长度都不超过30。一个目录下的子目录个数和文件个数之和不超过30。
输出
在显示一个目录中内容的时候，先显示其中的子目录（如果有的话），然后再显示文件（如果有的话）。文件要求按照名字的字母表的顺序显示（目录不用按照名字的字母表顺序显示，只需要按照目录出现的先后显示）。对每一组测试数据，我们要先输出"DATA SET x:"，这里x是测试数据的编号（从1开始）。在两组测试数据之间要输出一个空行来隔开。
你需要注意的是，我们使用一个'|'和5个空格来表示出缩排的层次。
'''

#2200015507 王一粟
class Node:
    def __init__(self,value):
        self.val = value
        self.file = []
        self.dir = []
    def get_value(self):
        return self.val
my_tag = " "
cnt = 0
def output(my_root):
    file_doc = sorted(my_root.file, key = lambda x:x.get_value())
    dir_doc = my_root.dir
    result_list = []
    for element in dir_doc:
        result_list.append("|"+5*my_tag+element.get_value())
        addi = ["|"+5*my_tag + i for i in output(element)]
        result_list.extend(addi)
    for element in file_doc:
        result_list.append(element.get_value())
    return result_list

while True:
    cnt += 1
    s = input()
    root_node = Node("root")
    stack = [root_node]
    if s == "#":
        break
    if s[0] == "f":
        current_node = Node(s)
        root_node.file.append(current_node)
    else:
        current_node = Node(s)
        root_node.dir.append(current_node)
        stack.append(current_node)
    while True:
        s = input()
        if s == "*":
            break
        if s[0] == "f":
            current_node = Node(s)
            stack[-1].file.append(current_node)
        elif s[0] == "d":
            current_node = Node(s)
            stack[-1].dir.append(current_node)
            stack.append(current_node)
        else:
            stack.pop()
    if cnt != 1:
        print()
    print(f"DATA SET {cnt}:")
    print("ROOT")
    end_list = output(root_node)
    for content in end_list:
        print(content)