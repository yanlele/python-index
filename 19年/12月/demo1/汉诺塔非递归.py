# coding=utf-8

def cal(num):
    '''
    计算整数的奇偶性
    :param num:
    :return:True表示奇数，False表示偶数
    '''
    return num % 2


def compareTwoNum(num1, num2):
    '''
    比较两个数的奇偶像是否相同
    :param num1:
    :param num2:
    :return: True表示相同，False表示不同
    '''
    return cal(num1) == cal(num2)


def movePan(tower, src, dst):
    '''
    把初始柱子最上面的盘子移动到目标柱子上
    :param tower:汉诺塔
    :param src:初始柱子
    :param dst:目标柱子
    :return:移动过后的汉诺塔
    '''
    move_value = tower[src].pop()
    tower[dst].append(move_value)
    print('{} {}==>{} moveValue:{}'.format(moveCount, src, dst, move_value))
    for key, value in tower.items():
        print(key + ':' + str(value))
    return tower


def calSrcAndDst(num, panNO, src):
    '''
    根据盘子号、盘子数量与初始柱子计算盘子移动的目标柱子与临时柱子
    :param num:盘子数量
    :param panNO:移动的盘子号
    :param src:移动盘子所在的柱子
    :return:移动盘子的初始柱子、目标柱子、临时柱子
    '''
    if compareTwoNum(num, panNO):
        # 盘子号与盘子数都是奇偶相同时，移动方向是：ACBACBAC逆时针方向移动
        if src == str_A:
            dst = str_C
            tmp = str_B
        elif src == str_B:
            dst = str_A
            tmp = str_C
        else:
            dst = str_B
            tmp = str_A
    else:
        # 盘子号与盘子数都是奇偶不同时，移动方向是：ABCABC顺时针方向移动
        if src == str_A:
            dst = str_B
            tmp = str_C
        elif src == str_B:
            dst = str_C
            tmp = str_A
        else:
            dst = str_A
            tmp = str_B
    return src, dst, tmp


def checkPanIsNull(tower, str_X):
    '''
    检查汉诺塔某个柱子是否有盘子
    :param tower:汉诺塔
    :param str_X:需要检查的柱子
    :return:
    '''
    return len(tower[str_X])


def calSecandSrcAndDst(tower, check_src_res, check_tmp_res, src_1, tmp_1):
    '''
    计算第二次移动的初始柱子和目标柱子
    :param check_src_res:检查第一次移动的初始柱子是否为空的结果
    :param check_tmp_res:检查第一次移动的临时柱子是否为空的结果
    :param src_1:第一次移动的初始柱子
    :param tmp_1:第一次移动的临时柱子
    :return:返回第二次移动的初始柱子与目标柱子
    '''
    if check_src_res and check_tmp_res:
        # 第一次移动的初始柱子和第一次移动的临时柱子都不为空
        # 比较两个柱子最上面的盘子号，较小的盘子号所在柱子为第二次移动的初始柱子，另外一个柱子是临时柱子
        src_top_value = tower[src_1][-1]
        tmp_top_value = tower[tmp_1][-1]
        if src_top_value < tmp_top_value:
            src_2, dst_2 = src_1, tmp_1
        else:
            src_2, dst_2 = tmp_1, src_1
        return src_2, dst_2
    else:
        if not check_src_res and not check_tmp_res:
            # 第一次移动的初始柱子和第一次移动的临时柱子都为空
            pass
        else:
            # 第一次移动的初始柱子和第一次移动的临时柱子有且只有一个为空
            if check_src_res:
                # 初始柱子不为空
                return src_1, tmp_1
            if check_tmp_res:
                # 临时柱子不为空
                return tmp_1, src_1


def nextMove(tower, src_1, dst_1, tmp_1):
    '''
    一个组合里面的第二次移动盘子
    :param tower:汉诺塔
    :param src_1:第一次移动的初始柱子
    :param dst_1:第一次移动的目标柱子
    :param tmp_1:第一次移动的临时柱子
    :return:移动过后的汉诺塔
    '''
    '''
    第2次移动的临时柱子是第1次1号盘子的目标柱子；
        除了第1次1号盘子的目标柱子的另外两个住找第二次移动的盘子：
            1.有一个柱子为空
                不为空的柱子最上面的盘子移动到另一个柱子上
            2.两个柱子都不为空
                比较两个柱子最上面的盘子号，把小的盘子移动到另一个柱子上
            3.两个柱子都为空（最开始和移动完成才存在），移动过程中不考虑这种情况
    '''
    tmp_2 = dst_1
    check_src_res = checkPanIsNull(tower, src_1)
    check_tmp_res = checkPanIsNull(tower, tmp_1)
    src_2, dst_2 = calSecandSrcAndDst(tower, check_src_res, check_tmp_res, src_1, tmp_1)
    tower = movePan(tower, src_2, dst_2)
    return tower


def hannio(num, src, dst, tmp):
    tower = {src: list(range(n, 0, -1)), tmp: [], dst: []}

    while len(tower[dst]) < num:
        '''
        盘子移动规律：
        1.盘子号与盘子数都是奇偶相同时，移动方向是：ACBACBAC逆时针方向移动
          盘子号与盘子数都是奇偶不同时，移动方向是：ABCABC顺时针方向移动
        2.每2次移动看成一个组合：
            第1次移动一号盘子
            第2次移动的临时柱子是第1次1号盘子的目标柱子；
            除了第1次1号盘子的目标柱子的另外两个住找第二次移动的盘子：
                1.有一个柱子为空
                    不为空的柱子最上面的盘子移动到另一个柱子上
                2.两个柱子都不为空
                    比较两个柱子最上面的盘子号，把小的盘子移动到另一个柱子上
                3.两个柱子都为空（最开始和移动完成才存在），移动过程中不考虑这种情况
        '''
        # 每2次移动看成一个组合
        # 第1次移动src上的1号盘子
        panNO = tower[src][-1]
        src_1, dst_1, tmp_1 = calSrcAndDst(num, panNO, src)
        tower = movePan(tower, src_1, dst_1)
        global moveCount
        moveCount += 1
        if len(tower[dst_1]) == num:
            break
        # 第2次移动盘子
        tower = nextMove(tower, src_1, dst_1, tmp_1)
        moveCount += 1
        # 下一次组合第一次移动的初始柱子是当前这一次组合第一次移动的目标柱子
        src = dst_1


n = 5
str_A = 'A'
str_B = 'B'
str_C = 'C'
moveCount = 1  # 移动次数
hannio(n, str_A, str_C, str_B)
