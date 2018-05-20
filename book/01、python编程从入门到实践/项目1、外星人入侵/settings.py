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
