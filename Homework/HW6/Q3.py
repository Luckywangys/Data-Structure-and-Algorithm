'''
描述
定义一个数组，初始化为空。在数组上执行两种操作：
1、增添1个元素，把1个新的元素放入数组。
2、输出并删除数组中最小的数。
使用堆结构实现上述功能的高效算法。
输入
第一行输入一个整数n，代表操作的次数。
每次操作首先输入一个整数type。
当type=1，增添操作，接着输入一个整数u，代表要插入的元素。
当type=2，输出删除操作，输出并删除数组中最小的元素。
1<=n<=100000。
输出
每次删除操作输出被删除的数字。
'''
#2200015507 王一粟
class heap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0
    def insert(self,k):
        self.heap_list.append(k)
        self.current_size += 1
        self.up(self.current_size)
    def up(self,i):
        while i//2>0:
            if self.heap_list[i] < self.heap_list[i//2]:
                self.heap_list[i],self.heap_list[i//2] = self.heap_list[i//2],self.heap_list[i]
            else:
                break
            i = i//2
    def del_min(self):
        if self.current_size > 1:
            a = self.heap_list[1]
            self.heap_list[1] = self.heap_list.pop()
            self.current_size -= 1
            self.down(1)
            return a
        elif self.current_size == 1:
            a = self.heap_list[1]
            self.heap_list.pop()
            self.current_size = 0
            return a

    def down(self,i):
        while i*2 <= self.current_size:
            if i*2+1>self.current_size:
                if self.heap_list[i]>self.heap_list[i*2]:
                    self.heap_list[i],self.heap_list[i*2]=self.heap_list[i*2],self.heap_list[i]
                break
            else:
                if self.heap_list[i*2]<self.heap_list[i*2+1]:
                    mc = i*2
                else:
                    mc = i*2+1
                if self.heap_list[mc]<self.heap_list[i]:
                    self.heap_list[mc],self.heap_list[i] = self.heap_list[i],self.heap_list[mc]
                    i = mc
                else:
                    break
n = int(input())
mylist = heap()
for _ in range(n):
    s = input()
    if s == "2":
        print(mylist.del_min())
    else:
        type_num,add_num = [int(i) for i in s.split()]
        mylist.insert(add_num)