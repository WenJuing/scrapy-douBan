import random


class guessNum(object):
    def __init__(self):
        self.answer = random.randint(1, 101)
        self.run()

    def run(self):
        i = 0
        while True:
            print("猜这个随机数，0-100")
            str_num = input("请输入可能的值：")
            i += 1
            try:
                if int(str_num) > self.answer:
                    print("大了")
                    continue
                elif int(str_num) < self.answer:
                    print("小了")
                    continue
                else:
                    print("恭喜你猜对了~")
                    print("你总共猜了%d" % i)
                    break
            except ValueError:
                print("要求输入整数")
                continue
            print("你真他娘的天才！")


if __name__ == '__main__':
    gn = guessNum()
