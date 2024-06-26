'''
描述
给定一些文档，要求求出某些单词的倒排表。
对于一个单词，它的倒排表的内容为出现这个单词的文档编号。
输入
第一行包含一个数N，1 <= N <= 1000，表示文档数。
接下来N行，每行第一个数ci，表示第i个文档的单词数。接下来跟着ci个用空格隔开的单词，表示第i个文档包含的单词。文档从1开始编号。1 <= ci <= 100。
接下来一行包含一个数M，1 <= M <= 1000，表示查询数。
接下来M行，每行包含一个单词，表示需要输出倒排表的单词。
每个单词全部由小写字母组成，长度不会超过256个字符，大多数不会超过10个字符。
输出
对于每一个进行查询的单词，输出它的倒排表，文档编号按从小到大排序。
如果倒排表为空，输出"NOT FOUND"。
'''

#2200015507 王一粟
n = int(input())
mydict = {}
for i in range(1,n+1):
    s = input().split()
    for element in s[1:]:
        if element in mydict:
            mydict[element].append(i)
        else:
            mydict[element] = [i]
m = int(input())
for _ in range(m):
    to_find = input()
    if to_find in mydict:
        print(" ".join(str(i) for i in sorted(set(mydict[to_find]))))
    else:
        print("NOT FOUND")