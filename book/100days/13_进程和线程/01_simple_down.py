from random import randint
from time import time, sleep


def download_task(filename):
    print('开始下载%s.....' % filename)
    time_to_download = randint(4, 10)
    sleep(time_to_download)
    print('%s下载完成！ 耗时 %d 秒' % (filename, time_to_download))


def main():
    start = time()
    download_task('Python 入门.pdf')
    download_task('xxxxx.avi')
    end = time()
    print('总共耗时 %.2f 秒' % (end - start))


if __name__ == '__main__':
    main()
