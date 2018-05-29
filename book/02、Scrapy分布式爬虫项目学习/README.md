# Scrapy分布式爬虫项目学习       

**目录**
- [第三章、爬虫基础知识](#class03)


## <div id='class03'>第三章、爬虫基础知识</div>

### 正则表达式专题         
模式：     
`re.match('模式字符串', '需要匹配的字符换')`返回的是一个布尔类型       

1、特殊字符          

|符号|含义|     
|:-|:-|     
|^|以什么字符开头开头，放在最前面|       
|.|表示任意字符|      
|*|前面那个字符可以重复N多次|       
|&|表示结尾字符，放在最后面|            
|?|强制正则匹配为非贪婪模式|
|+|前面的字符至少出现一次|
|{n}|前面字符至少出现n次|
|{n,}|前面字符至少出现n次以上|
|{n,m}|前面字符至少出现n次，最多出现m次|
| /| |这个是一个或的关系，两边之间任意成立就成立|
|[]|满足中括号中的任意一个字符就成立,这样也是可以的[0-9][a-zA-Z][^1], 而且中括号包括的字符就不在具有特殊意义了，就是普通字符|
|[^...]|不在[]中的字符：[^abc] 匹配除了a,b,c之外的字符|
|\s|匹配任意空白字符，等价于 [\t\n\r\f].|
|\S|匹配任意非空字符|
|\w|匹配字母数字及下划线|
|\W|匹配非字母数字及下划线|
|\d|匹配任意数字，等价于 [0-9]|
|\D|匹配任意非数字|

实例1：            
```python
import re

line = "bobby123"
regex_str = '^b.*3$'
if re.match(regex_str, line):
    print('yes')
```

实例2：关于？非贪婪模式的匹配,如下实例，我们这样期望可以拿到括号之间的内容，但实际上是只能拿到 'bb'，原因是正则表达式是一个默认贪婪模式，从后向前匹配的；         
```python
import re
line = 'booooobby123'
regex_str = '.*(b.*b).*'
match_obj = re.match(regex_str, line)
if match_obj:
    print(match_obj.group(1))
```

实例3：关于？非贪婪模式的匹配,如下实例，我们就可以拿到我们所需要的字符串了         
```python
import re
line = 'booooobby123'
regex_str = '.*?(b.*?b).*'
match_obj = re.match(regex_str, line)
if match_obj:
    print(match_obj.group(1))
```

实例4：+号          
```python
import re
line = 'booobbbaaaoobbbbbby123'
regex_str = '.*(b.+b).*'
match_obj = re.match(regex_str, line)
if match_obj:
    print(match_obj.group(1))
```
关于group()方法的使用，index，从最外成开始读取走的，下标为1开始

实例5：[]的使用          
```python
import re
line = '15213491241'
regex_str = '(1[245789][0-9]{9})'
match_obj = re.match(regex_str, line)
if match_obj:
    print(match_obj.group(1))
```


