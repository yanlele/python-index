# 在字典中存列表
# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushrooms', 'extra cheese'],
# }
# print('you order a ' + pizza['crust'] + '-crust pizza ' + 'with the flowing toppings: ' )
# for topping in pizza['toppings']:
#     print('\t' + topping)


# 嵌套示例2
# favorite_languages = {
#     'jen': ['python', 'ruby'],
#     'sarah': ['c'],
#     'edward': ['ruby', 'go'],
#     'phil': ['python', 'haskell'],
# }
# for name, languages in favorite_languages.items():
#     print('\n' + name.title() + "'s favorite languages are: ")
#     for language in languages:
#         print('\t' + language.title())


# 字典中存储字典
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for username,user_info in users.items():
    print('\nUsername: ' + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print('\tFull name: ' + full_name.title())
    print('\tLocation: ' + location.title())
