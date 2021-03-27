class showTuple(object):
    def __init__(self):
        self.T1 = ()
        self.createTuple()  # 创建元组
        self.subTuple(self.T1)  # 元组分片
        self.tuple2List(self.T1)  # 元组、列表转换

    def createTuple(self):
        print("创建元组：")
        self.T1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        print(self.T1)
        print("\n")

    def subTuple(self, Tuple):
        print("元组分片：")
        print("取元组第2个到最后一个：")
        print(self.T1[1:])
        print("取元组第2个到倒数第二个：")
        print(self.T1[1:-1])
        print("取元组第2个到最后一个，步长为2：")
        print(self.T1[1:-1:2])
        print("\n")

    def tuple2List(self, Tuple):
        print("元组转换成列表：")
        L2 = list(self.T1)
        print(L2)
        print("追加一个11：")
        L2.append(11)
        print(L2)
        print("列表转换成元组：")
        self.T1 = tuple(L2)
        print(self.T1)
        print("\n")


if __name__ == "__main__":
    st = showTuple()
