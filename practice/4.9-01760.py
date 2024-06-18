'''
描述
Hacker Bill has accidentally lost all the information from his workstation's hard drive and he has no backup copies of its contents. He does not regret for the loss of the files themselves, but for the very nice and convenient directory structure that he had created and cherished during years of work. Fortunately, Bill has several copies of directory listings from his hard drive. Using those listings he was able to recover full paths (like "WINNT\SYSTEM32\CERTSRV\CERTCO~1\X86") for some directories. He put all of them in a file by writing each path he has found on a separate line. Your task is to write a program that will help Bill to restore his state of the art directory structure by providing nicely formatted directory tree.
输入
The first line of the input file contains single integer number N (1 <= N <= 500) that denotes a total number of distinct directory paths. Then N lines with directory paths follow. Each directory path occupies a single line and does not contain any spaces, including leading or trailing ones. No path exceeds 80 characters. Each path is listed once and consists of a number of directory names separated by a back slash ("\").
Each directory name consists of 1 to 8 uppercase letters, numbers, or the special characters from the following list: exclamation mark, number sign, dollar sign, percent sign, ampersand, apostrophe, opening and closing parenthesis, hyphen sign, commercial at, circumflex accent, underscore, grave accent, opening and closing curly bracket, and tilde ("!#$%&'()-@^_`{}~").
输出
Write to the output file the formatted directory tree. Each directory name shall be listed on its own line preceded by a number of spaces that indicate its depth in the directory hierarchy. The subdirectories shall be listed in lexicographic order immediately after their parent directories preceded by one more space than their parent directory. Top level directories shall have no spaces printed before their names and shall be listed in lexicographic order. See sample below for clarification of the output format.
'''

#2200015507 王一粟
def output(node,k):
    if k != -1:
        print(" "*k+node.get())
    the_list = sorted(node.child.items(),key = lambda x:x[0])
    mylist = [i[1] for i in the_list]
    for element in mylist:
        output(element,k+1)
class Node:
    def __init__(self,val):
        self.val = val
        self.child = {}
    def get(self):
        return self.val
root = Node("root")
n = int(input())
for _ in range(n):
    lists = input().split("\\")
    current_node = root
    for content in lists:
        if content in current_node.child:
            current_node = current_node.child[content]
        else:
            new_node = Node(content)
            current_node.child[content] = new_node
            current_node = new_node
output(root,-1)