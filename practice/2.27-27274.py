'''
描述
一天，小北心血来潮，把自己的密码藏在了一串长长的字符串里，请你帮他找到提炼密码的方法吧。字符串s由ASCII的数字和大小写字母组成的，需要按照以下方式提炼出密码：
第一步：将字符串s的第20,21,22,...,2m（索引从1开始，下同）个字符提取出来。其中m=floor(log2(n))，floor(x)表示不大于x的最大整数
第二步：将提取出来的字符按以下方式重新排列：s[20], s[2m], s[21], s[2m-1], s[22], s[2m-2],...
如果经过第一步提取出的字符是0、1、2、3、4，那么重新排列后是：04132；
如果经过第一步提取出的字符是0、1、2、3、4、5，那么重新排列后是：051423。
这样，你就获得了小北的密码！
输入
一个字符串 s (字符串的长度大于0，小于 10^5)
输出
提炼出的密码 s'
'''

#2200015507 王一粟
s = input()
cnt = len(s)
m = 0
while True:
    if cnt == 1:
        break
    else:
        m = m+1
        cnt = cnt//2
mylist = []
for i in range(m+1):
    mylist.append(s[2**i-1])
result = ""
k = 0
while len(mylist) >= 1:
    if k == 0:
        result = result + mylist[0]
        del mylist[0]
        k = 1
    else:
        k = 0
        result = result + mylist[len(mylist)-1]
        del mylist[len(mylist)-1]
print(result)


