'''
描述
在数字安全领域，MD5加密是一种广泛使用的哈希算法，用于将任意长度的数据“压缩”成128位的加密串（通常表示为32位的十六进制数）。尽管MD5因安全漏洞而不再推荐用于敏感加密场合，它在教学和非安全领域的应用仍然广泛。你的任务是实现一个MD5加密验证系统，用于比较两串文本是否具有相同的MD5加密值。
输入
首先输入一个整数T，表示接下来有T组输入，其中T小于等于10。
接着是T组输入，每组输入包含两行，分别代表两串需要进行MD5加密比较的文本。每行文本的长度不超过1000个字符。
输出
对于每组输入，输出一行结果。如果两串文本的MD5加密值相同，则输出"Yes"；否则输出"No"。
'''

#2200015507 王一粟
import hashlib
t = int(input())
for _ in range(t):
    data1 = input()
    data2 = input()
    md5_hash1 = hashlib.md5(data1.encode()).hexdigest()
    md5_hash2 = hashlib.md5(data2.encode()).hexdigest()
    if md5_hash1 == md5_hash2:
        print("Yes")
    else:
        print("No")