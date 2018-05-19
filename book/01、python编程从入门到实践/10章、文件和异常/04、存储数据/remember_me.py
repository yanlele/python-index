# import json
#
# username = input('你的名字是什么呢？')
# filename = 'username.json'
# with open(filename, 'w') as f_obj:
#     json.dump(username, f_obj)
#     print('已经记住你的名字了！')

# import json
# filename = 'username.json'
#
# try:
#     with open(filename) as f_obj:
#         username = json.load(f_obj)
# except FileNotFoundError:
#     username = input('你的名字是什么呢？ ：')
#     with open(filename, 'w') as f_obj:
#         json.dump(username, f_obj)
#         print('名字已经存储好了')
# else:
#     print('读取到你的名字是' + username + ' !')


import json


def greet_user():
    """问候用户，并且指出其名字"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        print('没有找到相对应的文件，这个开始重新储存')
        username = input('请输入您的名字')
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print('你的名字存储好了')
    else:
        print('读取到你的名字是' + username + ' !')


greet_user()
