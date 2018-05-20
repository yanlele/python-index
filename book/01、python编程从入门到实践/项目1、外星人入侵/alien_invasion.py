import sys
import pygame

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

    # 开始游戏主循环
    while True:
        # 监听键盘和鼠标
        gf.check_events(ship)

        # 更新键盘操作来控制飞船
        ship.update()

        # 每次循环都需要重绘屏幕 而且 让最近回执的屏幕可见
        gf.update_screen(ai_settings, screen, ship)


run_game()
