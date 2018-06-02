# Scrapy分布式爬虫项目学习       

**目录**
- [第三章、爬虫基础知识](#class03)
    - [1、正则表达式专题](#class03-01)
- [第四章、scrapy爬取致命技术文章网站](#class04)


## <div id='class03'>第三章、爬虫基础知识</div>

### <div id='class03-01'>1、正则表达式专题</div>         
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
| | |这个是一个或的关系，两边之间任意成立就成立|
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

[实例6：一个复杂情况下提取出生日期的情况](./03章、爬虫基础知识/01、regtest/test/test.py)            
```python
import re

line = 'XXX出生于2001年6月1日'
line = 'XXX出生于2001/6/1'
line = 'XXX出生于2001-6-1'
line = 'XXX出生于2001-06-01'
line = 'XXX出生于2001-06'
line = 'XXX出生于2001-06月'
regex_str = '.*出生于(\d{4}[年/-]\d{1,2}([月/-]\d{1,2}|[月/-]$|$))'
match_obj = re.match(regex_str, line)
if match_obj:
    print(match_obj.group(1))
```

### <div id='class03-01'>1、深度优先</div>                 


## <div id='class04'>04章、scrapy爬取致命技术文章网站</div>  
### 1、安装scrapy 
如果scrapy安装失败，我们可以选择离线安装           
- [python离线安装包](https://www.lfd.uci.edu/~gohlke/pythonlibs/)
- [解决pip安装速度过慢的问题](../../18年/05月/02、解决pip安装速度过慢的问题/)

安装好了之后我们可以通过scrapy 这个命令来初始化我们的scrapy项目目录：           
例如： `scrapy startproject ArticleSpider`             

在这之后，我们还可以通过：
```
You can start your first spider with:
    cd ArticleSpider
    scrapy genspider example example.com
```
这样来创建我们所需要爬取网站的一个python 模板: `scrapy genspider jobbole blog.jobbole.com`         

### 2、爬虫项目的开始：抓取一篇文章             
**2.1、我们首先可以写一个测试的文件，文件中直接调用jobbole.py就可以达到调试的目的了**             
在测试文件main.py中，有这样一段代码：          
```python
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
```
用这个写法，可以暂时把我们文件目录添加到系统文件目录下面去； `os.path.abspath(__file__)`这个是获取当前文件路径， `os.path.dirname(os.path.abspath(__file__))` 这个是获取的父级文件路径， `sys.path.append(path)`这样就可以路径添加到系统配置中去了              

我们启动scrapy 爬虫项目的时候用到的命令行是： `scrapy crawl jobbole` 最后一个参数表示项目文件，但是一般在windows系统中是会启动失败的，这个时候我们需要安装一个模块文件：          
`pip install pypiwin32`

在测试文件main.py中测试代码如下：            
```python
from scrapy.cmdline import execute

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy", "crawl", "jobbole"])
```
我们可以打断点调试，就可以看到jobbole.py中response的一些列信息了

**2.2、xpath**                
基础语法            

|表达式|说明|
|:-|:-|
|article|选取所有article元素的所有子节点|
|/article|选取根元素article|
|article/a|选取所有属于article的子元素的a元素|
|//div|选取所有div子元素（无论出现在文档的任何地方）|
|article//div|选取所有属于article元素的后代的div元素，不管他出现在article之下的任何位置|
|//@class|选取所有名为class的属性|

xpath语法 - 谓语                   

|表达式|说明|
|:-|:-|
|/article/div[1]|选取属于article子元素的第一个div元素|
|/article/div[last()]|选取属于article子元素的最后一个div元素|
|/article/div[last()-1]|选取属于article子元素的倒数第二个div元素|
|//div[@lang]|选取所有拥有lang属性的div元素|
|//div[@lang='eng']|选取所有lang属性为eng的div元素|

xpath语法 - 其他

|表达式|说明|
|:-|:-|
|/div/*|选取属于div元素的所有子节点|
|//*|选取所有元素|
|//div[@*]|选取所有带属性的标签元素|
|/div/a或者//div/p|选取所有div元素的a和p元素|
|//span或者//ul|选取文档中的span和ul元素|
|article/div/p或者//span|选取所有article元素的div元素的p元素，一级文档中所有span元素|

补充：由于markdown语法限制，上述“或者”实际上是 “|”

**2.3、通过xpath来抓取节点的一个简单实例**             
```python
import scrapy


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com/']
    start_urls = ['http://blog.jobbole.com/113665/']

    def parse(self, response):

        re_select =  response.xpath('//*[@id="post-113665"]/div[1]/h1')
        pass
```
比如我们要抓取 `http://blog.jobbole.com/113665/` 这个网址下面的某一些信息， 直接设置urls, 然后通过response内置的xpath来赛选就可以了。（获取xpath其实可以直接在浏览器上获取就可以了）            
当然我们还可以在提取过程中，用很多种写法，这样可以大大的简化我们的选择xpath            
```python
re1_select = response.xpath('/html/body/div[1]/div[3]/div[1]/div[1]/h1')
re2_select = response.xpath('//*[@id="post-113665"]/div[1]/h1')
re3_select = response.xpath('//div[@class="entry-header"]/h1')
```

我们可以这样，拿到我们所需要的文本值： `response.xpath('//div[@class="entry-header"]/h1/text()').extract()[0]`             

其实我们这样调试时很慢的，我们可以利用控制台命令行进行调试：  `scrapy shell http://blog.jobbole.com/113665/` 这样我们就可以在脚本中调试了               

通过xpath提取文章完成， 具体代码如下：          
```python
# -*- coding: utf-8 -*-
import re
import scrapy


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com/']
    start_urls = ['http://blog.jobbole.com/110287/']

    def parse(self, response):
        re1_select = response.xpath('/html/body/div[1]/div[3]/div[1]/div[1]/h1')
        re2_select = response.xpath('//*[@id="post-113665"]/div[1]/h1')

        # 获取文章的title
        title = response.xpath('//div[@class="entry-header"]/h1/text()').extract()[0]

        # 获取文章的创建时间
        create_time = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()').extract()[0].strip().replace('·', '').strip()

        # 获取文章的点赞数
        praise_nums = int(response.xpath("//span[contains(@class, 'vote-post-up')]/h10/text()").extract()[0])

        # 收藏数量
        fav_nums = response.xpath("//span[contains(@class, 'bookmark-btn')]/text()").extract()[0]
        match_re = re.match('.*(\d+).*', fav_nums)
        if match_re:
            fav_nums = match_re.group(1)
        else:
            fav_nums = 0

        # 评论数
        comment_num = response.xpath("//a[@href='#article-comment']/span/text()").extract()[0]
        match_re = re.match('.*(\d+).*', comment_num)
        if match_re:
            comment_num = match_re.group(1)
        else:
            comment_num = 0

        # 获取文章正文 - 这个地方我们可以直接把html字符串提取出来就完了
        content = response.xpath("//div[@class='entry']").extract()[0]

        # 获取文章关键字
        tag_list = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/a/text()').extract()
        tag_list = [element for element in tag_list if not element.strip().endswith("评论")]
        tags = ','.join(tag_list)
        
        pass
```          
[xpath爬取数据实例](./ArticleSpider/ArticleSpider/spiders/jobbole.py)


**2.4、通过css选择器爬取数据的实现**
 
**利用css选择器**
[css选择器爬取数据实例](./ArticleSpider/ArticleSpider/spiders/jobbole_css_selecter.py)

备注：     
**使用extract()[0]的时候是有风险的，因为有的时候，有可能没有获取到数组，然后去第一个数组元素，是会抛出异常的， 我们可以使用 extract_first() 方法来代替extract()[0]**               


### 抓取多篇文章





