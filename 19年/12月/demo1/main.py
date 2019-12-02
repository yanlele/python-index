def hanoi(n):
    tower_belong = [0] * n  # 用列表开辟 n 个空间，用于存放 n 个金片各自的编号，编号对应塔号
    # 金片移动，编号对应更改
    if n % 2 == 0:  # 金片数量不同，塔的排序不同
        tower_name = ['A', 'B', 'C']  # 若 n 为偶数，最终所有金片恰好能移到右塔
    else:
        tower_name = ['A', 'C', 'B']  # 若 n 为奇数，最终所有金片会移到中塔
        # 用“轮换对称”将 B、C 两塔互换名字，以实现“负负得正”
    for step in range(1, 2 ** n):  # n 片金片最少需要移动 2^n - 1 次
        bin_step = bin(step)  # 求得 step 的二进制数值
        gold_num = len(bin_step) - bin_step.rfind('1') - 1
        # 计算 step 末尾 0 的个数，得到金片编号；上面说的“规律一”
        # 如 step = 0b0001，则 step 末尾 0 的个数为 0，表示此刻应移动 0 号金片
        # 如 step = 0b0100，则 step 末尾 0 的个数为 2，表示此刻应移动 2 号金片，依此类推
        # rfind 是从 0 开始计数，所以再减个 1

        print(f"第{step:2} 步：移动 {str(gold_num)} 号金片，从 {tower_name[tower_belong[gold_num]]} 塔到", end=' ')  # 移出金片的塔
        if gold_num % 2 == 0:  # 若 num 为 偶数，则右移
            tower_belong[gold_num] = (tower_belong[gold_num] + 1) % 3
            # 若从 C 塔右移，则又回到了 A 塔
        else:  # 若 num 为奇数，则左移
            tower_belong[gold_num] = (tower_belong[gold_num] + 2) % 3
            # 若从 A 塔左移，则又去到了 C 塔
        print(tower_name[tower_belong[gold_num]], '塔')  # 移入金片的塔


hanoi(5)
