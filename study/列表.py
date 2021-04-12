ls = ['ability', 'bias', 'cilicon']

print(ls)

# 根据下标删除
del ls[0]
print(ls)
# 根据值删除
ls.remove('cilicon')
print(ls)

ls2 = [1, 5, 3, 9, 6]

print(ls)

# sort()永久性排序
ls2.sort()
print(ls2)
# 传入参数reverse = Ture，逆向排序
ls2.sort(reverse=True)
print(ls2)

ls3 = ['a', 'd', 'c', 'b']
# sorted()临时性排序
print(ls3)
print(sorted(ls3))
print(ls3)

ls4 = [5, 3, 2, 6]
# reverse()倒置元素位置
print(ls4)
ls4.reverse()
print(ls4)
ls4.reverse()
print(ls4)

# 使用range()生成列表
ls5 = list(range(1, 11))
print(ls5)
even = list(range(2, 11, 2))
print(even)

# 列表解析生成列表
square = [value**2 for value in range(1, 11)]
print(square)

# 复制列表
my_food = ['apple', 'banana', 'cucumber']
print(my_food)
friend_food = my_food[:]    # 必须切片，直接赋值只是获取了地址，前者改变而后者也会跟着改变
print(friend_food)
my_food.append('ice-cream')
print(my_food)
friend_food.append('hotdog')
print(friend_food)

# 判断特定值在列表中
if 'apple' in my_food:
    print("在")
# 判断特定值不在列表中
if 'aaa' not in my_food:
    print("不在")
