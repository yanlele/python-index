import sys
import pygame

from settings import Settings
from ship import Ship

def run_game():
    # 初始化屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # 创建一艘飞船
    ship = Ship(screen)

    # 开始游戏主循环
    while True:

        # 监听键盘和鼠标
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 每次循环都需要重绘屏幕
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # 让最近回执的屏幕可见
        pygame.display.flip()


run_game()
