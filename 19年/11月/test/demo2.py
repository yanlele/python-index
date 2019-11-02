"""
二：
1.银行卡开户:
随机生成10位数卡号，输入用户信息（身份证号，交易密码，初始金额）
2.取款过程是这样的：
首先提示用户卡号和输入密码(pakaword),
先验证卡号是否存在：存在继续交易，否则结束交易或者进入开户界面
密码最多只能输入3次，超过3次见提   示用户"密码错误,请取卡” 结束交易。
如果用户密码码正确，再提示用户输入金额(amount).
只能输出100元的纸币， 一次取钱数要求最低0元，最高1000元。
如果用户输入的金额符合上述要求。则打印出用户取的钱数。
最后提示用户“交易完成，请取卡”，否则提示用户重新输入金额。
"""

import random

bankCardInfo = {}

while True:
    resStr = input('1：表示开户，\t2表示存/取钱\t3表示结束交易：')
    if resStr == '1':
        print('开户操作')
        identity_card = int(input("请输入身份证号："))
        pwd = int(input("请输入交易密码："))
        money = int(input("请输入初始金额："))

        # 生成随机10位数卡号
        card_number = str(random.randint(1000000000, 9999999999))

        bankCardInfo[card_number] = {
            "identity_card": identity_card,
            "pwd": pwd,
            "money": money,
        }

        print("你的账户信息: ", {card_number: bankCardInfo[card_number]})

    elif resStr == '2':
        print('存/取钱操作')
        '''
        输入卡号：
        输入密码：密码最多只能输入3次，超过3次见提   示用户"密码错误,请取卡” 结束交易
        '''
        card_number = str(input("请输入卡号："))

        if card_number in bankCardInfo.keys():
            print('存在账号')
        else:
            print('不存在当前账号')
            break

        # 获取开户信息
        current_card_info = bankCardInfo[card_number]

        count = 0
        condition = 1
        while count < 3:
            pwdRes = int(input('输入密码：'))

            print("card_Info: ", current_card_info)

            # 密码匹配
            if current_card_info['pwd'] != pwdRes:
                print("输入密码不正确， 请重新输入")
                count += 1
            else:
                break

        #     取钱环节
        '''
        只能输出100元的纸币， 一次取钱数要求最低0元，最高1000元。
        如果用户输入的金额符合上述要求。则打印出用户取的钱数。
        最后提示用户“交易完成，请取卡”，否则提示用户重新输入金额
        '''

        print("密码正确， 可以开始取钱了")
        print("只能输出100元的纸币， 一次取钱数要求最低0元，最高1000元。")
        print()

        get_money = int(input("请输入你要取的金额： "))
        while get_money < 0 & get_money > 1000 & get_money % 100 == 0:
            get_money = int(input("请重新输入金额："))

        current_money = current_card_info['money'] - get_money

        print("用户取出了： %d 元" % get_money)

        bankCardInfo['card_number'] = {
            "money": current_money,
        }

        print("你的账户余额以及账户信息如下： ", {card_number: bankCardInfo['card_number']})
        print("交易完成，请取卡")
        break


    elif resStr == '3':
        break
    else:
        print('输入错误，请重新输入')
