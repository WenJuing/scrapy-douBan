# 创建Dog类

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


# 根据类创建实例

my_dog = Dog('petter', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog's age is " + str(my_dog.age) + ".")

# 调用方法

my_dog.sit()
my_dog.roll_over()

# 直接修改属性的值

my_dog.age = 7
print("My dog's age is " + str(my_dog.age) + ".")

# 通过方法修改值

my_dog.update_age(8)
print("My dog's age is " + str(my_dog.age) + ".")
my_dog.update_age(7)
print("My dog's age is " + str(my_dog.age) + ".")

# 继承


class SmartDog(Dog):
    '''较聪明的狗'''

    def __init__(self, name, age):
        super().__init__(name, age)  # 注意，这里不需要self参数
        self.IQ = 'high'    # 新增属性

    def show_IQ(self):  # 新增方法
        '''展示IQ'''
        print(self.name + "'s IQ is " + self.IQ + ".")

    def describe_dog(self):     # 重写方法
        '''新的输出小狗信息'''
        print("Smart dog's name is " + self.name.title() +
              ",IQ is", self.IQ + " and age is " + str(self.age) + ".")


my_smart_dog = SmartDog('greey', 12)
my_smart_dog.describe_dog()
my_smart_dog.show_IQ()

# 将实例用作属性


class InfoSys():
    '''小狗的信息系统'''

    def __init__(self, is_adopt=False):
        self.is_adopt = is_adopt

    def show_god_info(self):
        '''显示领养状态'''
        if self.is_adopt:
            print("The dog is adopted.")
        else:
            print("The dog is exiling")

    def describe_dog(self):
        '''新的输出小狗信息'''
        print("Smart dog's name is " + self.name.title() +
              ",IQ is", self.IQ + " and age is " + str(self.age) + ".")

    def add_age(self, age):
        '''递增年龄'''
        self.age += age


class SmartDog(Dog):
    '''较聪明的狗'''

    def __init__(self, name, age, is_adopt):
        super().__init__(name, age)
        self.IQ = 'high'
        self.info = InfoSys(is_adopt)   # 将其他实例用作属性

    def show_IQ(self):
        '''展示IQ'''
        print(self.name + "'s IQ is " + self.IQ + ".")


my_smart_dog = SmartDog('hahaha', 22, 'True')
my_smart_dog.info.show_god_info()
