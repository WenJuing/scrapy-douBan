class showDict(object):
    def __init__(self):
        self.leiMu = self.createDict()  # 创建字典
        self.insertDict(self.leiMu)  # 插入元素
        self.modifyDict(self.leiMu)  # 修改元素
        self.operationDict(self.leiMu)  # 字典操作
        self.deleteDict(self.leiMu)  # 删除元素

    def createDict(self):
        print('创建字典：')
        leiMu = {'name': '雷姆', 'age': 16, 'color': '蓝色'}
        print(leiMu)
        print('\n')
        return leiMu

    def insertDict(self, leiMu):
        print('插入元素：')
        leiMu['speak'] = '今天天气真晴朗呢~'
        print(leiMu)
        print('\n')

    def modifyDict(self, leiMu):
        print('修改元素：')
        leiMu['speak'] = '等下一起回去吧~'
        print(leiMu)
        print('\n')

    def operationDict(self, leiMu):
        print('字典操作：')
        print('1）返回所有keys值')
        print(leiMu.keys())
        print('2）返回所有values值')
        print(leiMu.values())
        print('3）返回所有(key,value)值')
        print(leiMu.items())
        print("4）输出key为speak的值")
        print(leiMu['speak'])
        print(leiMu.get('speak'))
        print(leiMu.get('speak2', '未找到该值'))
        print("\n")

    def deleteDict(self, leiMu):
        print('删除字典')
        del(leiMu)
        try:
            print(leiMu)
        except NameError:
            print('leiMu 未被定义')


if __name__ == '__main__':
    sd = showDict()
