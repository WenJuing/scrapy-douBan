import sys

class ColorPrint(object):
    def __init__(self):
        self.color = "red"
        self.msg = "cao"
        self.cPrint()

    def cPrint(self):
        colors = {
            'black': '\033[1;30;47m',
            'red': '\033[1;31;47m',
            'green': '\033[1;32;47m',
            'yellow': '\033[1;33;47m',
            'blue': '\033[1;34;47m',
            'white': '\033[1;37;47m'}
        while self.msg != 'exit':
            print("输入exit退出程序")
            self.color = input("输入颜色：")
            self.msg = input("输入文字：")
            if self.color not in colors.keys():
                print("输入的颜色暂时没有，按系统默认配置的颜色打印")
                continue
            else:
                print("输入的颜色有效，开始彩色打印")
            print("%s%s" % (colors[self.color],self.msg))
            print("\033[0m")


if __name__ == '__main__':
    cp = ColorPrint()