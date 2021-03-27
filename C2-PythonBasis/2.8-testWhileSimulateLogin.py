import getpass


class FakeLogin(object):
    def __init__(self):
        self.name = 'king'
        self.password = 'no'
        self.banner = 'hello, you have login system!'
        self.run()

    def run(self):
        print("只有一个用户King")
        print("偷偷告诉你，密码为88888888哟~")
        while True:
            print("Login:king")
            pw = getpass.getpass("password：")
            if pw == '88888888':
                print("%s" % self.banner)
                print("退出程序")
                exit()
            else:
                if len(pw) > 12:
                    print("密码长度应该小于12")
                    continue
                elif len(pw) < 6:
                    print("密码长度应该大于6")
                    continue
                else:
                    print("密码错误，继续猜")
                    continue


if __name__ == '__main__':
    fl = FakeLogin()
