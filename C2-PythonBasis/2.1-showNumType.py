# 各种数据类型的输出

class ShowNumType(object):
    def __init__(self):
        self.showInt()
        self.showFloat()
        self.showComplex()

    def showInt(self):
        print("十进制的整型")
        print("%d" % (10))
        print("二进制的整型")
        print("%s" % (bin(10)))
        print("八进制的整型")
        print("%s" % (oct(10)))
        print("十六进制的整型")
        print("%s" % (hex(10)))

    def showFloat(self):
        print("显示浮点数")
        print("%.2f" % (10.123))

    def showComplex(self):
        var = 3 + 4j
        print("显示复数")
        print("%d %d" % (var.real, var.imag))


if __name__ == '__main__':
    showNum = ShowNumType()
