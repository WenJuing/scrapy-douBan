# 演示新类的继承

class Spider(object):
    '''蜘蛛子，最原始的蜘蛛形态'''
    eyes = 4
    legs = 8
    weight = 0.02
    iq = '低下'

    def __init__(self):
        '''初始化'''
        self.name = '蜘蛛子'
        self.show()

    def show(self):
        print("我叫%s" % self.name)
        print("我有%d个眼睛和%d条腿，体重为%.2f，智力%s" % (self.eyes, self.legs, self.weight, self.iq))
        print("\n")


class BigSpider(Spider):
    '''于原本小小的蜘蛛相比，体积猛增了好几倍'''
    eyes = 6
    weight = 5.55
    iq = '一般'

    def __init__(self):
        self.name = '巨型蜘蛛'
        self.show()


class SmallSipder(BigSpider):
    '''着重于智慧与灵敏度，智慧上升体重反而减少'''
    legs = 10
    weight = 2.33
    iq = '较高'

    def __init__(self):
        self.name = '智慧蜘蛛子'
        self.show()


class MaxSpider(SmallSipder):
    '''终极进化'''
    eyes = 10
    weight = 3.12
    iq = '无所不知'

    def __init__(self):
        self.name = '蜘蛛女王'
        self.show()


if __name__ == '__main__':
    spider = Spider()
    bigSpider = BigSpider()
    smallSipder = SmallSipder()
    maxSpider = MaxSpider()
