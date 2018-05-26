class Settings():
    """储存本项目的所有设置的类"""

    def __init__(self):
        """初始化有的的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船的设置 控制移动速度
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # 子弹的设置
        self.bullet_speed_factor = 3  # 子弹速度
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3   # 允许子弹的最大数量

        #  外星人设置
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 5
        # fleet_direction 为 1 表示向右移，为 -1 表示向左移
        self.fleet_direction = 1

