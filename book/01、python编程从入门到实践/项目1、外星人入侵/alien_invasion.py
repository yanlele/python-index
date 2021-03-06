import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from ship import Ship
from alien import Alien
import game_functions as gf


def run_game():
    # 初始化屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # 创建一个用于存储游戏信息的实例
    stats = GameStats(ai_settings)

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建一个用于存储子弹的编辑组
    bullets = Group()

    # 创建一个用于存储外星人的编辑组
    aliens = Group()

    #  创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏主循环
    while True:
        # 监听键盘和鼠标
        gf.check_events(ai_settings, screen, ship, bullets)

        if stats.game_active:
            # 更新键盘操作来控制飞船
            ship.update()

            # 更新子弹相关的逻辑
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)

            # 更新每个外星人的位置
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        # 每次循环都需要重绘屏幕 而且 让最近回执的屏幕可见
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
