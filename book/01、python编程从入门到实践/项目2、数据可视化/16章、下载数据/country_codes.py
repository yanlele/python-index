"""获取两个字母的国别码
书中本来是pygal.i18n这个包中导入，不过因为COUNTRIES已经被删除了
所以我们重新从pygal_maps_world包中导入
"""
from pygal_maps_world.i18n import COUNTRIES


def get_country_code(country_name):     # get_country_code() 接受国家名，并将其存储在形参country_name 中
    """根据指定的国家，返回Pygal使用的两个字母的国别码"""
    for code, name in COUNTRIES.items():        # 我们遍历COUNTRIES 中的国家名—国别码对
        if name == country_name:        # 如果找到指定的国家 名，就返回相应的国别码
            return code
    # 如果没有找到指定的国家，就返回None
    return None     # 在循环后面，我们在没有找到指定的国家名时返回None


print(get_country_code('Andorra'))
print(get_country_code('United Arab Emirates'))
print(get_country_code('Afghanistan'))
