# unconfirmed_users = ['alice', 'brian', 'candace']
# confirmed_users = []
# # 验证每个用户，直到没有未验证用户为止
# # 将每个经过验证的列表都移到已验证用户列表中
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#     print("Verifying user: " + current_user.title())
#     confirmed_users.append(current_user)
# # 显示所有已验证的用户
# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())


# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)
# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)

# 使用用户输入来填充字典
responses = {}
flag = True
while flag:
    name = input('请输入你的名字')
    response = input('请输入你的答案')
    responses[name] = response
    repeat = input('是否继续下一个人问答？yes/no')
    if (repeat != 'yes'):
        flag = False
for name, response in responses.items():
    print(name, response)
