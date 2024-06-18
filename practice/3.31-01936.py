'''
描述
你设计了一个新的加密技术，可以用一种聪明的方式在一个字符串的字符间插入随机的字符串从而对信息进行编码。由于专利问题，我们将不会详细讨论如何在原有信息中产生和插入字符串。不过，为了验证你的方法，有必要写一个程序来验证原来的信息是否全在最后的字符串之中。
给定两个字符串s和t，你需要判断s是否是t的“子列”。也就是说，如果你去掉t中的某些字符，剩下字符将连接而成为s。
输入
输入包括多个测试样例。每一个都是由空格分隔的由字母数字ASCII字符组成的两个特定的字符串s和t。s和t的长度不超过100000。
输出
对于每个测试样例，如果s是t的“子列”，则输出”Yes”，否则输出”No”
'''

#2200015507 王一粟
def to_find(sub,find):
    i,j = 0,0
    length1 = len(sub)
    length2 = len(find)
    while i<length1 and j<length2:
        if sub[i] == find[j]:
            i += 1
            j += 1
        else:
            j+=1
    if i==length1:
        return "Yes"
    else:
        return "No"
while True:
    try:
        sub1,find1 = input().split()
        result = to_find(sub1,find1)
        print(result)
    except:
        break