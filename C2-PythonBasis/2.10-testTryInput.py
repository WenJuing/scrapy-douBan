class tryInput(object):
    def __init__(self):
        self.len = 10
        self.numList = self.createList()
        self.getNum()
    
    def createList(self):
        print("现在创建一个长度为%d的数字列表" % self.len)
        numL = []
        while len(numL) < 10:
            str_n = input("请输入一个整数：")
            try:
                n = int(str_n)
            except ValueError:
                print("输入错误，要求是输入一个整数")
                continue
            numL.append(n)
            print("现在的列表为：")
            print(numL)
        return numL

    def getNum(self):
        print("当前列表为")
        print(self.numList)
        inStr = None
        while inStr != 'EXIT':
            print("输入EXIT退出程序")
            inStr = input("输入列表下标[-10, 9]：")
            try:
                index = int(inStr)
                num = self.numList[index]
                print("列表中下标为%d的值为%d" % (index, num))
            except ValueError:
                print("输入错误，列表的下标是一个整数")
                continue
            except IndexError:
                print("下标太大，访问列表超出范围")
                continue


if __name__ == '__main__':
    tl = tryInput()
