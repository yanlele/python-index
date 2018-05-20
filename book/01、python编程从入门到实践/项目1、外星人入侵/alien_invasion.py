import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # 初始化屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建一个用于存储子弹的编辑组
    bullets = Group()

    # 开始游戏主循环
    while True:
        # 监听键盘和鼠标
        gf.check_events(ai_settings, screen, ship, bullets)

        # 更新键盘操作来控制飞船
        ship.update()

        # 将子弹存储到编组中
        bullets.update()

        # 删除已经消失的子弹
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)

        # 每次循环都需要重绘屏幕 而且 让最近回执的屏幕可见
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
