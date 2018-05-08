# 简单的返回值示例
# def get_name(first_name, last_name):
#     full_name = first_name + last_name
#     return full_name
#
#
# musican = get_name('yan', 'le')
# print(musican)


# 8.3.2 　让实参变成可选的
# def get_name (first_name, last_name, middle_name):
#     if middle_name:
#         full_name = first_name + middle_name +last_name
#     else:
#         full_name = first_name + middle_name
#     return full_name
#
#
# my_name = get_name('yan ', 'le', 'le')
# print(my_name)


# 返回字典
# def build_person(first_name, last_name):
#     person = {'first_name': first_name, 'last_name': last_name}
#     return person
#
#
# get_person = build_person('yanle', 'le')
# print(get_person)

# 结合使用函数和 while  循环
def get_name(first_name, last_name):
    return first_name + last_name


while True:
    print('输入你的名字')
    print('输入q退出程序')
    first_name = input('First name: ')
    if first_name == 'q':
        break
    last_name = input('Last name: ')
    if last_name == 'q':
        break
    full_name = get_name(first_name, last_name)
    print(full_name)