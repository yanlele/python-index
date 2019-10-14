# Scrapy分布式爬虫项目学习       

**目录**
- [第三章、爬虫基础知识](#class03)
    - [1、正则表达式专题](#class03-01)
    - [2、2、深度优先](#class03-02)
- [第四章、scrapy爬取技术文章网站](#class04)
    - [1、安装scrapy](#class04-01)
    - [2、爬虫项目的开始：抓取一篇文章](#class04-02)
    - [3、抓取多篇文章](#class04-03)
    - [4、文章存储问题](#class04-04)
    - [5、scrapy:item loader机制](#class04-05)
- [第五章、scrapy爬取问答网站](#class05)
    - [1、requests模拟登陆](#class05-01)
    - [2、scrapy模拟登陆](#class05-02)
    - [3、内容的爬取](#class05-03)
- [第六章、CrawlSpider整站爬取](#class06)
    - [1、数据表的设计](#class06-01)
    - [2、具体爬虫代码的实现和数据的入库](#class06-02)


## <div id='class03'>第三章、爬虫基础知识</div>

### <div id='class03-01'>1、正则表达式专题</div>         
模式：     
`re.match('模式字符串', '需要匹配的字符换')`返回的是一个布尔类型       

**特殊字符**                             

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
regex_str = '^b.*3$'  # b 开头； 任意字符可以重复n 次； 3 结尾
if re.match(regex_str, line):
    print('yes')
```

实例2：关于？非贪婪模式的匹配,如下实例，我们这样期望可以拿到括号之间的内容，但实际上是只能拿到 'bb'，原因是**正则表达式是一个默认贪婪模式，从后向前匹配的**；         
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

### <div id='class03-02'>2、深度优先</div>                 


## <div id='class04'>04章、scrapy爬取致命技术文章网站</div>  
### <div id='class04-01'>1、安装scrapy</div> 
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

### <div id='class04-02'>2、爬虫项目的开始：抓取一篇文章</div>             
- 2.1、我们首先可以写一个测试的文件，文件中直接调用jobbole.py就可以达到调试的目的了             
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

- 2.2、xpath                
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

- 2.3、通过xpath来抓取节点的一个简单实例             
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
调试的目录为：  `D:\yanle\web\python\python-index\book\02、Scrapy分布式爬虫项目学习>`

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


- 2.4、通过css选择器爬取数据的实现
 
**利用css选择器**
[css选择器爬取数据实例](./ArticleSpider/ArticleSpider/spiders/jobbole_css_selecter.py)

备注：     
**使用extract()[0]的时候是有风险的，因为有的时候，有可能没有获取到数组，然后去第一个数组元素，是会抛出异常的， 我们可以使用 extract_first() 方法来代替extract()[0]， extract_first()还可以接受一个参数，就是没有找到对象的时候，用接受参数来代替就可以了。**               


### <div id='class04-03'>3、抓取多篇文章</div>                 

```python
from scrapy.http import Request
from urllib import parse

"""skip"""

def parse(self, response):
    """
    1、获取文章列表页面的具体文章url并交给scrapy下载，然后交给解析函数进行具体字段的解析
    2、获取下一页的url 并交给scrapy进行下载，下载完成之后交给parse函数
    """
    # 解析列表页中的所有文章url并交给scrapy下载后并进行解析
    post_urls = response.css("#archive div.floated-thumb .post-thumb a::attr(href)").extract()
    for post_url in post_urls:
        yield Request(url=parse.urljoin(response.url, post_url), callback=self.parse_detail, dont_filter=True)

    # 提取下一页交给 scrapy 来进行下载
    next_urls = response.css('a.next.page-numbers::attr(href)').extract_first("")
    if next_urls:
        yield Request(url=parse.urljoin(response.url, next_urls), callback=self.parse)
```
其中 `parse_detail` 方法，就是我们上面用到的那个获取具体文章的实现           
还有一个很重要的地方: [关于scrapy - Request 中的回调函数不执行 的问题研究](https://blog.csdn.net/honglicu123/article/details/75453107) ` dont_filter=True`                
[Scrapy-Request和Response（请求和响应）模块的研究](https://blog.csdn.net/weixin_37947156/article/details/74974208)                       

### <div id='class04-04'>4、文章存储问题</div>                 
> 关于items的使用，我们可以在这里实现具体提取的文章字段逻辑

这个地方要介绍一下Request 模块中 meta的使用，meta接受的是一个对象字典，可以直接带到response中去。通过这个原则，我们可以获取到一片文章的title 图片。                   
```python
"""skip"""
post_nodes = response.css("#archive div.floated-thumb .post-thumb a")
for post_node in post_nodes:
    image_url = post_node.css("img::attr(src)").extract_first("")
    post_url = post_node.css("::attr(href)").extract_first("")
    url = parse.urljoin(response.url, post_url)         # 这个会自动帮我们拼接我们想要的url地址： parse.urljoin(base_url, url)
    yield Request(url=url, callback=self.parse_detail, meta={"front_image_url": image_url}, dont_filter=True)
         
"""skip"""
# 获取文章的点赞数
praise_nums = int(response.xpath("//span[contains(@class, 'vote-post-up')]/h10/text()").extract()[0])
```

在items.py文件中，定义一个接受我们要指定保存的内容字段                    
```python
class JobBoleArticleItem(scrapy.Item):
    title = scrapy.Field()  # 只能指定这个类型
    create_date = scrapy.Field()
    url = scrapy.Field()
    url_object_url = scrapy.Field()
    font_image_url = scrapy.Field()
    font_image_path = scrapy.Field()  # 本地存储路径
    praise_nums = scrapy.Field()
    comment_num = scrapy.Field()
    fav_nums = scrapy.Field()
    tags = scrapy.Field()
    content = scrapy.Field()
```

然后把我们这个定义好的类，注入到spiders.py中去，用于保存相关数据               

> 关于自动获取图片，然后保存的中间件问题：              

首先要处理settings里面的配置：         
```python
ITEM_PIPELINES = {
    'ArticleSpider.pipelines.ArticlespiderPipeline': 300,
    'scrapy.pipelines.images.ImagesPipeline': 1
}
IMAGES_URLS_FIELD = "font_image_url"        # 需要保存图片的字段，需要注意的是，要接受的是一个数组
project_dir = os.path.abspath(os.path.dirname(__file__))        # 获取当前文件的路径的父级路径
IMAGES_STORE = os.path.join(project_dir, 'images')              # 获取保存图片的路径
IMAGES_MIN_HEIGHT = 100     # 下载的图片最小的高度
IMAGES_MIN_WIDTH = 100      # 下载的图片最小宽度
```
这个配置的数值，越小就越先执行，这样我们就可以自动获取图片然后保存了                 

- 处理图片保存的路径，跟我们本地路径绑定起来，然后再保存到font_image_path里面储存起来                     
这个时候我们就要建立自己的pipelines了             
```python
from scrapy.pipelines.images import ImagesPipeline
class ArticleImagePipeline(ImagesPipeline):
```
定义的对象继承了ImagesPipeline， 首先看看里面有什么重要的用法：                 
`get_media_requests`:           
`item_completed`: 重载这个方法之后我们可以冲这个文件中获取到我们实际的下载地址            
我们这里就要用到重载方法 `item_completed`:          
```python
from scrapy.pipelines.images import ImagesPipeline
class ArticleImagePipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        # 我们可以通过results 来获取到文件的实际存储路径
        for ok,value in results:
            image_file_path = value["path"]
        item["font_image_path"] = image_file_path
        
        return item
```
在settings.py设置文件中，做如下的设置修改：               
```python
ITEM_PIPELINES = {
    'ArticleSpider.pipelines.ArticlespiderPipeline': 300,
    # 'scrapy.pipelines.images.ImagesPipeline': 1,
    'ArticleSpider.pipelines.ArticleImagePipeline': 1
}
```
这样之后，在再打个个断点在 `pipelines.ArticlespiderPipeline` 的return item 身上，这个时候，我们就可以这个front_image_path                

>　对url做一个MD5 编码，减少url占用的存储空间                

我们先要定义一个公共的方法，做md5的转换工作：路径为 `ArticleSpider/ArticleSpider/utils/common.py`           
```python
import hashlib

def get_md5(url):
    if isinstance(url, str):
        url = url.encode("urf-8")
    m = hashlib.md5()
    m.update(url)
    return m.hexdigest()
```

**存储到json中去：**                              
这个时候我们将我们定义好的方法，导入到 `spiders/jobbole.py文件中去`：               
```python
from ArticleSpider.utils.common import get_md5
"""skip"""
article_item["url_object_id"] = get_md5(response.url)
```
这样就实现了我们MD5的转换，而且注入到了pipelines              

- 保存到数据库                
首先我们要在 `pipelines.py` 文件中定义一个数据转为json的类             
```python
import codecs
import json
class JsonWithEncodingPipeline(object):
    def __init__(self):
        self.file = codecs.open('article.json', 'w', encoding="utf-8")

    def process_item(self, item, spider):
        lines = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(lines)
        return item

    def spider_closed(self, spider):
        self.file.close()
```         
然后把这个pipelines的类，注入到settings里面去， 修改配置如下：            
```python
ITEM_PIPELINES = {
    # 'ArticleSpider.pipelines.ArticlespiderPipeline': 300,
    'ArticleSpider.pipelines.JsonWithEncodingPipeline': 2,
    # 'scrapy.pipelines.images.ImagesPipeline': 1,
    'ArticleSpider.pipelines.ArticleImagePipeline': 1
}
```
然后运行，就可以测试文件，就可以成功写入我们的json文件了              


> scrapy本身提供了写入文件的一种机制， 可以方便的将我们的items到处为任何文件                             

```python
from scrapy.exporters import JsonItemExporter
class JsonExporterPipeline(object):
    # 调用scrapy提供的json export到处json文件
    def __init__(self):
        self.file = open('articleExport.json', 'wb')
        self.exporter = JsonItemExporter(self.file, encoding="utf-8", ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
```
然后在 `settings.py` 文件中做如下的配置变更：      
```python
ITEM_PIPELINES = {
    # 'ArticleSpider.pipelines.ArticlespiderPipeline': 300,
    # 'ArticleSpider.pipelines.JsonWithEncodingPipeline': 2,
    'ArticleSpider.pipelines.JsonExporterPipeline': 2,
    # 'scrapy.pipelines.images.ImagesPipeline': 1,
    'ArticleSpider.pipelines.ArticleImagePipeline': 1
}
```
然后运行，就可以测试文件，就可以成功写入我们的json文件了，如果我们顺利的爬取到了所有的我们想要的数据之后，这个时候，程序会给我们前后多加一个大括号（方便数据的读取）；                                 

> **储存到数据库中**                   

在此之前，我们需要把我们保存的时间字符串转换为我们数据库能保存的时间对象            
```python
import datetime
"""skip"""
try:
    create_date = datetime.datetime.strptime(create_date, "%Y/%m/%d").date()
except Exception as e:
    create_date = datetime.datetime.now().date()
    article_item["create_date"] = create_date
"""skip"""
```

做如下的数据表结构设计，按着我们定义保存的字段来就好了：            
```sql
SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for article
-- ----------------------------
DROP TABLE IF EXISTS `article`;
CREATE TABLE `article` (
  `title` varchar(200) NOT NULL,
  `create_date` date DEFAULT NULL,
  `url` varchar(300) NOT NULL,
  `url_object_id` varchar(50) NOT NULL,
  `font_image_url` varchar(300) DEFAULT NULL,
  `font_image_path` varchar(200) DEFAULT NULL,
  `praise_nums` int(11) NOT NULL DEFAULT '0',
  `comment_num` int(11) NOT NULL DEFAULT '0',
  `fav_nums` int(11) NOT NULL DEFAULT '0',
  `tags` varchar(200) DEFAULT NULL,
  `content` longtext,
  PRIMARY KEY (`url_object_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

然后需要安装mysql的驱动: `pip install -i https://pypi.douban.com/simple/ mysqlclient`            
安装完成之后，可以在我们的pipeline中定义我们存储mysql的实现类了哟；            
```python
import MySQLdb
class MysqlPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect('127.0.0.1', 'root', '53693750', '0001_article_spider', charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        # jobbole_article
        insert_sql = """
            insert into jobbole_article(title, create_date, url, url_object_id, font_image_url, font_image_path, praise_nums, comment_num, fav_nums, tags, content)
            values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        self.cursor.execute(insert_sql, (item["title"], item["create_date"], item["url"], item["url_object_id"],
                                         item["font_image_url"], item["font_image_path"], item["praise_nums"],
                                         item["comment_num"], item["fav_nums"], item["tags"], item["content"]))
        self.conn.commit()
```

然后修改我们的settings:            
```python
ITEM_PIPELINES = {
    # 'ArticleSpider.pipelines.ArticlespiderPipeline': 300,
    # 'ArticleSpider.pipelines.JsonWithEncodingPipeline': 2,
    # 'ArticleSpider.pipelines.JsonExporterPipeline': 2,
    'scrapy.pipelines.images.ImagesPipeline': 1,
    'ArticleSpider.pipelines.ArticleImagePipeline': 2,
    'ArticleSpider.pipelines.MysqlPipeline': 3
}
```
然后执行测试文件sql， 就可以得到我们期望的数据了！                 


另外一种插入mysql数据库的方式： 异步插入数据（这种方式的好处是非阻塞性）                 
可以在我们的pipeline中定义我们存储mysql的实现类了，是通过Twisted实现的：              
第一步，我们可以将我们的mysql连接数据写到我们的settings里面去的。                 
```python
MYSQL_HOST = '127.0.0.1'
MYSQL_DBNAME = 'jobbole_article'
MYSQL_USER = 'root'
MYSQL_PASSWORD = '53693750'
```   

第二步，在pipelines中定义一个处理的处理异步插入的类              
```python
import MySQLdb
import MySQLdb.cursors
from twisted.enterprise import adbapi
class MysqlTwistedPipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbparms = dict(
            host=settings["MYSQL_HOST"],
            db=settings["MYSQL_DBNAME"],
            user=settings["MYSQL_USER"],
            passwd=settings["MYSQL_PASSWORD"],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True
        )
        dbpool = adbapi.ConnectionPool("MySQLdb", **dbparms)
        return cls(dbpool)

    def process_item(self, item, spider):
        # 使用twisted, 将mysql插入变为异步操作
        # jobbole_article
        query = self.dbpool.runInteraction(self.do_insert, item)
        query.addErrorback(self.handle_error, item, spider)     # 处理异常

    def handle_error(self, failure, item, spider):
        # 处理异步插入数据异常
        print(failure)

    def do_insert(self, cursor, item):
        # 这里实现具体的插入逻辑
        insert_sql = """
                    insert into jobbole_article(title, create_date, url, url_object_id, font_image_url, font_image_path, praise_nums, comment_num, fav_nums, tags, content)
                    values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
        cursor.execute(insert_sql, (item["title"], item["create_date"], item["url"], item["url_object_id"],
                                    item["font_image_url"], item["font_image_path"], item["praise_nums"],
                                    item["comment_num"], item["fav_nums"], item["tags"], item["content"]))
```

做完这些之后，最后在注入到settings中去：            
```python
ITEM_PIPELINES = {
    # 'ArticleSpider.pipelines.ArticlespiderPipeline': 300,
    # 'ArticleSpider.pipelines.JsonWithEncodingPipeline': 2,
    # 'ArticleSpider.pipelines.JsonExporterPipeline': 2,
    'scrapy.pipelines.images.ImagesPipeline': 1,
    'ArticleSpider.pipelines.ArticleImagePipeline': 2,
    # 'ArticleSpider.pipelines.MysqlPipeline': 3
    'ArticleSpider.pipelines.MysqlTwistedPipeline': 3
}
```

### <div id='class04-05'>5、scrapy:item loader机制</div>               
item_loader一共有三个比较重要的方法：            
`
item_loader.add_css()
item_loader.add_xpath()
item_loader.add_value()
`
首先我们需要在 `jobbole.py` 中定义我们的loader:              
```python
from ArticleSpider.items import JobBoleArticleItem
from scrapy.loader import ItemLoader

    """skip"""
    # 通过item_loader来加载loader
    item_loader = ItemLoader(item=JobBoleArticleItem(), response=response)
    item_loader.add_css("title", ".entry-header h1::text")
    item_loader.add_value("url", response.url)
    item_loader.add_value("url_object_id", get_md5(response.url))
    item_loader.add_css("create_date", "p.entry-meta-hide-on-mobile::text")
    item_loader.add_value("font_image_url", [font_image_url])
    item_loader.add_css("praise_nums", ".vote-post-up h10::text")
    item_loader.add_css("comment_num", "a[href='#article-comment'] span::text")
    item_loader.add_css("fav_nums", ".bookmark-btn::text")
    item_loader.add_css("tags", "p.entry-meta-hide-on-mobile a::text")
    item_loader.add_css("content", "div.entry")
    
    article_item = item_loader.load_item()
    
    # 传递到pipelines.py
    yield article_item
```
但是这样的拿到的数据，会有两个问题，第一个问题是我们拿到的数据是一个数组，第二个问题是我们拿到的数据，没有做任何处理。
为了解决这个问题，我们可以在items里面进行处理。

在 `items.py` 文件里面，我们item有一个方法Field(), 这个方法接受两个非常重要的参数：          
第一个是方法： `input_processor = MapCompose()`                
第二个是： `output_processor=TakeFirst()`           
我们在使用 `input_processor = MapCompose()` 的时候，首选需要导入一个这样的包 `from scrapy.loader.processors import MapCompose`。
然后`input_processor = MapCompose()` 里面可以接受一个lamba表达式，也可以接受一个函数，作为item的一个预处理方法！               
使用如下：               
```python
from scrapy.loader.processors import MapCompose
import scrapy

def add_jobbole(value):
    return value + '-le'


class JobBoleArticleItem(scrapy.Item):
    title = scrapy.Field(
        input_processor=MapCompose(lambda x: x + '-yan', add_jobbole)
    )  # 只能指定这个类型
    create_date = scrapy.Field()
    url = scrapy.Field()
    url_object_id = scrapy.Field()
    font_image_url = scrapy.Field()
    font_image_path = scrapy.Field()  # 本地存储路径
    praise_nums = scrapy.Field()
    comment_num = scrapy.Field()
    fav_nums = scrapy.Field()
    tags = scrapy.Field()
    content = scrapy.Field()
```

对于每一个字段，我们比如都想去取第一个参数，这个时候，就用用到Field的第二个参数了 `output_processor=TakeFirst()` ：            
```python
import scrapy
import datetime
from scrapy.loader.processors import MapCompose, TakeFirst
class JobBoleArticleItem(scrapy.Item):
    title = scrapy.Field(
        input_processor=MapCompose(lambda x: x + '-yan', add_jobbole),
        output_processor=TakeFirst()
    )  # 只能指定这个类型
    create_date = scrapy.Field(
        input_processor=MapCompose(date_convert),
        output_processor=TakeFirst()
    )
    url = scrapy.Field()
    url_object_id = scrapy.Field()
    font_image_url = scrapy.Field()
    font_image_path = scrapy.Field()  # 本地存储路径
    praise_nums = scrapy.Field()
    comment_num = scrapy.Field()
    fav_nums = scrapy.Field()
    tags = scrapy.Field()
    content = scrapy.Field()
```
但是我们如果我们所有字段都是希望去取第一个参数，每个字段都要加上这样的规则，会显得非常的麻烦。我们可以定义一个自己的loader来批量处理这个问题：              
```python
class ArticleItemLoader(ItemLoader):
    default_output_processor = TakeFirst()
```
这个时候我们实例化的时候，就不能用 `ItemLoader` 了，要用我们定义好的 `ArticleItemLoader`           
```python
font_image_url = response.meta.get("front_image_url", "")
item_loader = ArticleItemLoader(item=JobBoleArticleItem(), response=response)
item_loader.add_css("title", ".entry-header h1::text")
item_loader.add_value("url", response.url)
item_loader.add_value("url_object_id", get_md5(response.url))
item_loader.add_css("create_date", "p.entry-meta-hide-on-mobile::text")
item_loader.add_value("font_image_url", [font_image_url])
item_loader.add_css("praise_nums", ".vote-post-up h10::text")
item_loader.add_css("comment_num", "a[href='#article-comment'] span::text")
item_loader.add_css("fav_nums", ".bookmark-btn::text")
item_loader.add_css("tags", "p.entry-meta-hide-on-mobile a::text")
item_loader.add_css("content", "div.entry")

article_item = item_loader.load_item()

# 传递到pipelines.py
yield article_item
```

items定义内容如下：                
```python
def get_nums(value):
    match_re = re.match(".*?(\d+).*", value)
    if match_re:
        nums = int(match_re.group(1))
    else:
        nums = 0
    return nums


def date_convert(value):
    try:
        create_date = datetime.datetime.strptime(value, "%Y/%m/%d").date()
    except Exception as e:
        create_date = datetime.datetime.now().date()
    return create_date


def remove_comment_tags(value):
    #去掉tag中提取的评论
    if "评论" in value:
        return ""
    else:
        return value


def return_value(value):
    return value


class ArticleItemLoader(ItemLoader):
    default_output_processor = TakeFirst()


class JobBoleArticleItem(scrapy.Item):
    title = scrapy.Field()  # 只能指定这个类型
    create_date = scrapy.Field(
        input_processor=MapCompose(date_convert)
    )
    url = scrapy.Field()
    url_object_id = scrapy.Field()
    font_image_url = scrapy.Field(
        output_processor=MapCompose(return_value)   # 覆盖掉我们默认的 default_output_processor
    )
    font_image_path = scrapy.Field()  # 本地存储路径
    praise_nums = scrapy.Field(
        imput_process=MapCompose(get_nums)
    )
    comment_num = scrapy.Field(
        imput_process=MapCompose(get_nums)
    )
    fav_nums = scrapy.Field(
        imput_process=MapCompose(get_nums)
    )
    tags = scrapy.Field(
        input_processor=MapCompose(remove_comment_tags),
        output_processor=Join(",")
    )
    content = scrapy.Field()
```


## <div id='class05'>第五章、scrapy爬取问答网站</div>

### <div id='class05-01'>5.1、requests模拟登陆</div>                  
首先我们需要用到的是requests这个库，我们在这里查看文档手册 [快速上手 — Requests 2.18.1 文档](http://docs.python-requests.org/zh_CN/latest/user/quickstart.html)                
关于这个库的安装： `pip install requests` 直接这样就可以了              
然后在utils这个文件目录下面，创建文件login_requests.py，通过requests来完成模拟登陆              
```python
# -*- coding: utf-8 -*-
__author__ = 'YanLe'

import requests

try:
    import cookielib
except:
    import http.cookiejar as cookielib

import re

session = requests.session()
session.cookies = cookielib.LWPCookieJar(filename="cookies.txt")    #这个实例方法可以让我们直接可以保存我们的cookies文件
try:
    session.cookies.load(ignore_discard=True)
except:
    print("cookie未能加载")

agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"
header = {
    "HOST": "www.zhihu.com",
    "Referer": "https://www.zhizhu.com",
    'User-Agent': agent
}


def is_login():
    # 通过个人中心页面返回状态码来判断是否为登录状态
    inbox_url = "https://www.zhihu.com/question/56250357/answer/148534773"
    response = session.get(inbox_url, headers=header, allow_redirects=False)
    if response.status_code != 200:
        return False
    else:
        return True


def get_xsrf():
    # 获取xsrf code
    response = session.get("https://www.zhihu.com", headers=header)
    match_obj = re.match('.*name="_xsrf" value="(.*?)"', response.text)
    if match_obj:
        return (match_obj.group(1))
    else:
        return ""


def get_index():
    """
        请求首页， 把本地cookies写入request中
        这个时候回写入一个html文件，我们可以通过本地生成的html页面登陆页面
    """
    response = session.get("https://www.zhihu.com", headers=header)
    with open("index_page.html", "wb") as f:
        f.write(response.text.encode("utf-8"))
    print("ok")


def get_captcha():
    import time
    t = str(int(time.time() * 1000))
    captcha_url = "https://www.zhihu.com/captcha.gif?r={0}&type=login".format(t)
    t = session.get(captcha_url, headers=header)
    with open("captcha.jpg", "wb") as f:
        f.write(t.content)
        f.close()

    from PIL import Image
    try:
        im = Image.open('captcha.jpg')
        im.show()
        im.close()
    except:
        pass

    captcha = input("输入验证码\n>")
    return captcha


def zhihu_login(account, password):
    # 知乎登录
    # 判断登陆类型，是手机登陆还是邮箱登陆
    if re.match("^1\d{10}", account):
        print("手机号码登录")
        post_url = "https://www.zhihu.com/login/phone_num"
        post_data = {
            "_xsrf": get_xsrf(),
            "phone_num": account,
            "password": password,
            "captcha": get_captcha()
        }
    else:
        if "@" in account:
            # 判断用户名是否为邮箱
            print("邮箱方式登录")
            post_url = "https://www.zhihu.com/login/email"
            post_data = {
                "_xsrf": get_xsrf(),
                "email": account,
                "password": password
            }

    response_text = session.post(post_url, data=post_data, headers=header)
    session.cookies.save()


zhihu_login("18782902568", "admin123")
# get_index()
is_login()

# get_captcha()
```
运行这个python文件就可以了，实现模拟登陆；                


### <div id='class05-02'>5.2、scrapy模拟登陆</div>
直接塞spiders里面定义爬取规则的文件下面做处理就可以了
```python
    def start_requests(self):
        return [scrapy.Request('https://www.zhihu.com/#signin', headers=self.headers, callback=self.login)]

    def login(self, response):
        response_text = response.text
        match_obj = re.match('.*name="_xsrf" value="(.*?)"', response_text, re.DOTALL)
        xsrf = ''
        if match_obj:
            xsrf = (match_obj.group(1))

        if xsrf:
            post_url = "https://www.zhihu.com/login/phone_num"
            post_data = {
                "_xsrf": xsrf,
                "phone_num": "",
                "password": "",
                "captcha": ""
            }

            import time
            t = str(int(time.time() * 1000))
            captcha_url = "https://www.zhihu.com/captcha.gif?r={0}&type=login".format(t)
            yield scrapy.Request(captcha_url, headers=self.headers, meta={"post_data": post_data},
                                 callback=self.login_after_captcha)

    def login_after_captcha(self, response):
        with open("captcha.jpg", "wb") as f:
            f.write(response.body)
            f.close()

        from PIL import Image
        try:
            im = Image.open('captcha.jpg')
            im.show()
            im.close()
        except:
            pass

        captcha = input("输入验证码\n>")

        post_data = response.meta.get("post_data", {})
        post_url = "https://www.zhihu.com/login/phone_num"
        post_data["captcha"] = captcha
        return [scrapy.FormRequest(
            url=post_url,
            formdata=post_data,
            headers=self.headers,
            callback=self.check_login
        )]

    def check_login(self, response):
        # 验证服务器的返回数据判断是否成功
        text_json = json.loads(response.text)
        if "msg" in text_json and text_json["msg"] == "登录成功":
            for url in self.start_urls:
                yield scrapy.Request(url, dont_filter=True, headers=self.headers)
```

### <div id='class05-03'>5.3、网站内容的爬取</div>                  
首先我们进入shell测试的时候，因为这个网站需要user_agent才能访问，所以我们测试命令行的时候，也是需要加入user_agent，我们可以这样做：              
`scrapy shell -s USER_AGENT="Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0" https://www.zhizhu.com`      
调试的目录为：  `D:\yanle\web\python\python-index\book\02、Scrapy分布式爬虫项目学习>`                    

这个时候如果能打开网页，我们接下来可以吧网页内容写入到文件里面，然后通过分析文件来确立这个是否是新版本的网页知乎：               
```python
with open("e:/zhihu.html", "wb") as f:
    f.write(response.text.encode("utf-8"))
```
接下来的内容省略掉，因为知乎改版，而且用上面的方式，已经无法爬取知乎内容了。所以弃坑。


## <div id='class06'>第六章、CrawlSpider整站爬取</div>
### <div id='class06-01'>6.1、数据表的设计</div>
```
SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for lagou_job
-- ----------------------------
DROP TABLE IF EXISTS `lagou_job`;
CREATE TABLE `lagou_job` (
  `url` varchar(300) NOT NULL,
  `url_object_id` varchar(50) NOT NULL,
  `title` varchar(100) NOT NULL,
  `salary` varchar(20) DEFAULT NULL,
  `job_city` varchar(10) DEFAULT NULL,
  `work_years` varchar(100) DEFAULT NULL,
  `degree_need` varchar(30) DEFAULT NULL,
  `job_type` varchar(20) DEFAULT NULL,
  `publish_time` varchar(20) NOT NULL,
  `tags` varchar(100) DEFAULT NULL,
  `job_advantage` varchar(1000) DEFAULT NULL,
  `job_desc` longtext NOT NULL,
  `job_addr` varchar(50) DEFAULT NULL,
  `company_url` varchar(300) DEFAULT NULL,
  `company_name` varchar(100) DEFAULT NULL,
  `crawl_time` datetime NOT NULL,
  `crawl_update_time` datetime DEFAULT NULL,
  PRIMARY KEY (`url_object_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

### <div id='class06-02'>6.2、具体爬虫代码的实现和数据的入库</div>
- **实例化crawl 模板**
我们可以通过 `scrapy genspider --list` 来查看genspider给我们的磨人模板有哪些：           
```
Available templates:
  basic
  crawl
  csvfeed
  xmlfeed
```         
如果我们不指明，默认给我们生成的是basic, 如果我们需要的是一个crawl的模板，我们这一这样做： `scrapy genspider -t crawl lagou www.lagou.com`                 
这里需要注意的是我们实例化模板的路径： `D:\yanle\web\python\python-index\book\02、Scrapy分布式爬虫项目学习\ArticleSpider`                

执行完上面的命令行之后，我们就可以得到一个空的模板文件：                
```python
# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class LagouSpider(CrawlSpider):
    name = 'lagou'
    allowed_domains = ['www.lagou.com']
    start_urls = ['https://www.lagou.com/']

    rules = (
        Rule(LinkExtractor(allow=("zhaopin/.*",)), follow=True),            # 这里编写我们想爬取的url连接模式
        Rule(LinkExtractor(allow=("gongsi/j\d+.html",)), follow=True),
        Rule(LinkExtractor(allow=r'jobs/\d+.html'), callback='parse_job', follow=True),
    )

    def parse_job(self, response):
        # 解析拉勾网的所有职位
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
```

- **如果出现导包的问题，可以用这种方法来解决**
我们一settings.py文件作为例子                    
```python
import os
import sys
BASE_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'ArticleSpider'))
```
这样的操作就可以把文件加入到python Path中去了，就不会出现import找不到内容的情况了


- **定义items**                   
```python
class LagouJobItem(scrapy.Item):
    # 拉勾网职位信息
    title = scrapy.Field()
    url = scrapy.Field()
    url_object_id = scrapy.Field()
    salary = scrapy.Field()
    job_city = scrapy.Field(
        input_processor=MapCompose(remove_splash),
    )
    work_years = scrapy.Field(
        input_processor=MapCompose(remove_splash),
    )
    degree_need = scrapy.Field(
        input_processor=MapCompose(remove_splash),
    )
    job_type = scrapy.Field()
    publish_time = scrapy.Field()
    job_advantage = scrapy.Field()
    job_desc = scrapy.Field()
    job_addr = scrapy.Field(
        input_processor=MapCompose(remove_tags, handle_jobaddr),
    )
    company_name = scrapy.Field()
    company_url = scrapy.Field()
    tags = scrapy.Field(
        input_processor=Join(",")
    )
    crawl_time = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = """
            insert into lagou_job(title, url, url_object_id, salary, job_city, work_years, degree_need,
            job_type, publish_time, job_advantage, job_desc, job_addr, company_name, company_url,
            tags, crawl_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE salary=VALUES(salary), job_desc=VALUES(job_desc)
        """
        params = (
            self["title"], self["url"], self["url_object_id"], self["salary"], self["job_city"],
            self["work_years"], self["degree_need"], self["job_type"],
            self["publish_time"], self["job_advantage"], self["job_desc"],
            self["job_addr"], self["company_name"], self["company_url"],
            self["job_addr"], self["crawl_time"].strftime(SQL_DATETIME_FORMAT),
        )

        return insert_sql, params
```

spider里面的具体实现逻辑：            
```python
    def parse_job(self, response):
        #解析拉勾网的职位
        item_loader = LagouJobItemLoader(item=LagouJobItem(), response=response)
        item_loader.add_css("title", ".job-name::attr(title)")
        item_loader.add_value("url", response.url)
        item_loader.add_value("url_object_id", get_md5(response.url))
        item_loader.add_css("salary", ".job_request .salary::text")
        item_loader.add_xpath("job_city", "//*[@class='job_request']/p/span[2]/text()")
        item_loader.add_xpath("work_years", "//*[@class='job_request']/p/span[3]/text()")
        item_loader.add_xpath("degree_need", "//*[@class='job_request']/p/span[4]/text()")
        item_loader.add_xpath("job_type", "//*[@class='job_request']/p/span[5]/text()")

        item_loader.add_css("tags", '.position-label li::text')
        item_loader.add_css("publish_time", ".publish_time::text")
        item_loader.add_css("job_advantage", ".job-advantage p::text")
        item_loader.add_css("job_desc", ".job_bt div")
        item_loader.add_css("job_addr", ".work_addr")
        item_loader.add_css("company_name", "#job_company dt a img::attr(alt)")
        item_loader.add_css("company_url", "#job_company dt a::attr(href)")
        item_loader.add_value("crawl_time", datetime.now())

        job_item = item_loader.load_item()

        return job_item
```


- **插入数据库**
数据库的设计： 略                       
```python
    def get_insert_sql(self):
        insert_sql = """
            insert into lagou_job(title, url, url_object_id, salary, job_city, work_years, degree_need,
            job_type, publish_time, job_advantage, job_desc, job_addr, company_name, company_url,
            tags, crawl_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE salary=VALUES(salary), job_desc=VALUES(job_desc)
        """
        params = (
            self["title"], self["url"], self["url_object_id"], self["salary"], self["job_city"],
            self["work_years"], self["degree_need"], self["job_type"],
            self["publish_time"], self["job_advantage"], self["job_desc"],
            self["job_addr"], self["company_name"], self["company_url"],
            self["job_addr"], self["crawl_time"].strftime(SQL_DATETIME_FORMAT),
        )

        return insert_sql, params
```
其余的入库操作和第一个项目是一样的， 可以参见就可以了






