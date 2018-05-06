# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0['color'])
# print(alien_0['points'])

# 访问字典中的值
# alien_0 = {'color': 'green', 'points': 5}
# new_porints = alien_0['points']
# print('You just earned ' + str(new_porints) + ' points!')

# 添加键值对
# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

# 先创建空字典
# alien_0 = {}
# alien_0['color'] = 'green'
# alien_0['points'] = 5
# print(alien_0)

# 修改字典中的值
# alien_0 = {'color': 'green'}
# print("The alien is " + alien_0['color'] + ".")
# alien_0['color'] = 'yellow'
# print("The alien is now " + alien_0['color'] + ".")

# 一个数据字典相关的示例
# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# print("Original x-position: " + str(alien_0['x_position']))
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3
#
# alien_0['x_position'] = alien_0['x_position'] + x_increment
# print('NEW x-position: ' + str(alien_0['x_position']))

# 删除键值对
# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)
# del alien_0['points']
# print(alien_0)

# 便利所有的键值对
# user_0 = {
#     'username': 'efermi',
#     'first': 'enrico',
#     'last': 'fermi',
# }
# for key,value in user_0.items():
#     print('\nkey: ' + key)
#     print('value: ' + value)


# 遍历字典中的所有键
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }
# for name in favorite_languages.keys():
#     print(name.title())
# print(favorite_languages.keys())


# 按顺序遍历字典中的所有键
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }
# for name in sorted(favorite_languages.keys()):
#     print(name.title() + ", thank you for taking the poll.")

# 使用set() 祛除重复项
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("The following languages have been mentioned:")
for lang in set(favorite_languages.values()):
    print(lang.title())