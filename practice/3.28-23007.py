'''
描述
小Hi在一家互联网巨头公司实习。他发现由于公司不同的部门实在太多了，导致使用的一些开发工具和软件库的版本非常不统一、五花八门。
比如一款工具就有2.96, 3.4.5, 4.8.2, 6.4和7.2几种不同的版本。
现在给出了N个版本号，请你帮助小Hi把这些版本号从旧到新排序。
版本号格式都是若干由'.'连接起来的非负整数。比较版本号新旧时先主版本号(最左的整数)开始，再比较次版本号(第二个整数)，以此类推……。
例如2.96 < 3.4.5 < 4.8.2 < 4.8.4 < 4.13 < 6.4 < 7.2
特别的，我们认为NULL小于0，也即1.0 < 1.0.0，4.8.2 < 4.8.2.0。
输入
第一行包含一个整数N。 (1 ≤ N ≤ 100)
以下N行每行一个版本号。 版本号总长度不超过100，主版本号和每个子版本号的数值不超过100
输出
N行，每行一个版本号，从旧到新排列。
'''

#2200015507 王一粟
class F:
    def __init__(self,mylist):
        self.mylist = mylist
    def get(self):
        return ".".join(str(i) for i in self.mylist)
    def __lt__(self,other):
        list1 = self.mylist
        list2 = other.mylist
        length1 = len(list1)
        length2 = len(list2)
        i,j = 0,0
        while i < min(length1,length2):
            if list1[i] < list2[i]:
                return True
            if list1[i] > list2[i]:
                return False
            i += 1
        if length1 < length2:
            return True
        else:
            return False
n = int(input())
store_list = []
for _ in range(n):
    element = [int(i) for i in input().split(".")]
    f = F(element)
    store_list.append(f)
result_list = sorted(store_list)
for edition in result_list:
    print(edition.get())