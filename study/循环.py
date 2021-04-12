# while循环

""" message = ""
while message != 'exit':
    message = input()
    if message != 'exit':
        print(message) """

unconfirmed_user = ['leimu', 'lamu', 'amiliya']
confirmed_user = []

while unconfirmed_user:
    current_user = unconfirmed_user.pop()
    print("Vertify user", current_user)
    confirmed_user.append(current_user)
print("confirmed user:")
for user in confirmed_user:
    print(user.title())

# 删除包含特定值的所有列表元素

pets = ['dog', 'cat', 'cat', 'snack', 'cat', 'dog']

print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

# 用输入填充字典

response = {}
flag = 1
while flag:
    name = input("你的名字是？")
    answer = input("你最喜欢哪部动漫？")
    response[name] = answer
    flag = input("你还希望收取信息吗？（yes/no）")
    if flag == 'no':
        flag = 0
for name, answer in response.items():
    print(name + '最喜欢的动漫是' + answer)
