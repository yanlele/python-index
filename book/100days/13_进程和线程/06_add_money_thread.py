"""
下面的例子演示了100个线程向同一个银行账户转账（转入1元钱）的场景，在这个例子中，
银行账户就是一个临界资源，在没有保护的情况下我们很有可能会得到错误的结果。

运行下面的程序，结果让人大跌眼镜，100个线程分别向账户中转入1元钱，结果居然远远小于100元。
之所以出现这种情况是因为我们没有对银行账户这个“临界资源”加以保护，多个线程同时向账户中存钱时，
会一起执行到new_balance = self._balance + money这行代码，多个线程得到的账户余额都是初始状态下的0，
所以都是0上面做了+1的操作，因此得到了错误的结果。在这种情况下，“锁”就可以派上用场了。
我们可以通过“锁”来保护“临界资源”，只有获得“锁”的线程才能访问“临界资源”，
而其他没有得到“锁”的线程只能被阻塞起来，直到获得“锁”的线程释放了“锁”，其他线程才有机会获得“锁”，
进而访问被保护的“临界资源”。
"""

from time import sleep
from threading import Thread


class Account(object):

    def __init__(self):
        self._balance = 0

    def deposit(self, money):
        new_balance = self._balance + money
        sleep(0.01)
        self._balance = new_balance

    @property
    def balance(self):
        return self._balance


class AddMoneyThread(Thread):

    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)


def main():
    account = Account()
    threads = []
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print('账户余额为: ￥%d元' % account.balance)


if __name__ == '__main__':
    main()


