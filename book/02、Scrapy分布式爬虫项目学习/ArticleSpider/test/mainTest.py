import re

# match_re = re.match('.*(\d+).*', '3 评论')
# print(match_re)
# if match_re:
#     print(match_re.group(1))
# else:
#     print(match_re)


tag_list =['职场', ' 9 评论 ', '面试']
print([element for element in tag_list if not element.strip().endswith("评论")])