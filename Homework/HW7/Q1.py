'''
描述
给定一个句子，这个句子由若干个可能包含字母、数字和标点符号的单词组成，每两个单词之间有一个空格。请以单词为单位，倒序输出这个句子。
句中单词数不超过50，每个单词长度不超过10。
输入
一行，一句由若干个单词组成的句子
输出
一行，以单词为单位反转后得到的字符串
'''
#2200015507 王一粟
s = input().split()
s1 = s[::-1]
print(" ".join(s1))