'''一个关于狗的类'''


class Dog():
    '''一只可爱的小狗'''

    def __init__(self, name, age):  # 使用类时自动运行，接收参数并返回实例
        self.name = name
        self.age = age

    def sit(self):
        '''坐下命令'''
        print(self.name.title(), "is now sitting!")

    def describe_dog(self):
        '''输出小狗信息'''
        print("Dog's name is", self.name.title(),
              "and age is", str(self.age) + ".")

    def roll_over(self):
        '''打滚命令'''
        print(self.name.title(), "is rolled over!")

    def update_age(self, age):
        '''修改年龄'''
        if age > self.age:
            self.age = age
        else:
            print("You can't roll back age!")


'''一个关于聪明狗的类'''


class SmartDog(Dog):
    '''较聪明的狗'''

    def __init__(self, name, age, IQ='high'):
        super().__init__(name, age)  # 注意，这里不需要self参数
        self.IQ = IQ    # 新增属性

    def show_IQ(self):  # 新增方法
        '''展示IQ'''
        print(self.name + "'s IQ is " + self.IQ + ".")

    def describe_dog(self):     # 重写方法
        '''新的输出小狗信息'''
        print("Smart dog's name is " + self.name.title() +
              ",IQ is", self.IQ + " and age is " + str(self.age) + ".")
