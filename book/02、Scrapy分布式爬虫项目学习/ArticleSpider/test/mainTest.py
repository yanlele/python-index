import re

match_re = re.match('.*(\d+).*', '3 评论')
print(match_re)
if match_re:
    print(match_re.group(1))
else:
    print(match_re)
