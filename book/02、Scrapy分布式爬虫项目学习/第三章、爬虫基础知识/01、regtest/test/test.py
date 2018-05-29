import re

# line = "bobby123"
# regex_str = '^b.*3$'
# if re.match(regex_str, line):
#     print('yes')

line = '15213497741'
regex_str = '(1[245789][0-9]{9})'
match_obj = re.match(regex_str, line)
if match_obj:
    print(match_obj.group(1))