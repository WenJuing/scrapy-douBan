# 列表的使用


class showList(object):
    def __init__(self):
        self.L1 = []
        self.L2 = []

        self.createList()  # 创建列表
        self.insertData()  # 插入数据
        self.appendData()  # 追加数据
        self.deleteData()  # 删除数据
        self.subList()  # 列表分片

    def createList(self):
        print("1）生成数组L1、L2")
        self.L1 = list("abcdefg")
        for i in range(0, 10):
            self.L2.append(i)
        print("L1:%s" % self.L1)
        print("L2:%s" % self.L2)
        print("\n")

    def insertData(self):
        print("2）插入数据")
        self.L1.insert(2, 100)
        self.L2.insert(2, "python")
        print("L1的第三个位置插入100:%s" % self.L1)
        print("L2的第三个位置插入python:%s" % self.L2)
        print("\n")

    def appendData(self):
        print("3）追加数据")
        self.L1.append([1, 2, 3])
        self.L2.append(('a', 'b', 'c'))
        print("L1追加列表[1, 2, 3]:%s" % self.L1)
        print("L2追加元组('a', 'b', 'c'):%s" % self.L2)
        print("\n")

    def deleteData(self):
        print("4）删除数据")
        self.L1.pop(0)
        self.L1.pop()
        print("L1删除第一个和最后一个数据：%s" % self.L1)
        self.L2.pop(1)
        self.L2.pop(3)
        print("L2删除第2个和第4个数据：%s" % self.L2)
        print("\n")

    def subList(self):
        print("5）列表分片")
        print("L1取自第3个到最后一个：%s" % self.L1[2:])
        print("L2取自第2个到倒数第2个，步长为2：%s" % self.L2[1:-1:2])
        print("\n")


if __name__ == '__main__':
    sl = showList()
