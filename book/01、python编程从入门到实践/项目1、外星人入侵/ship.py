import pygame


class Ship():
    def __init__(self, ai_settings, screen):
        """初始化飞船并且设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像获得其外接举行
        self.image = pygame.image.load('./images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #  将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #  在飞船的属性 center 中存储小数值
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整"""
        #  更新飞船的 center 值，而不是 rect
        if self.moving_right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_right:
            self.center -= self.ai_settings.ship_speed_factor

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
