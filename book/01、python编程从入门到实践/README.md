# 《python编程从入门到实践》 [美]Eric Matthes著       袁国忠 译

目录：     
- [第 2  章　变量和简单数据类型](#class02)
- [第 3  章　列表简介](#class03)

## <div id='class02'>第 2  章　变量和简单数据类型</div>
### 2.3字符串
- 2.3.1、使用方法修改字符串的大小写         
对于字符串，可执行的最简单的操作之一是修改其中的单词的大小写。请看下面的代码，并尝试判断其作用：        
```python
name = "ada lovelace"
print(name.title())
```

要将字符串改为全部大写或全部小写，可以像下面这样做：      
```python
name = "Ada Lovelace"
print(name.upper())
print(name.lower())
```

- 2.3.2 　合并（拼接）字符串      
实例1：        
```python
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)
```

- 2.3.3 　使用制表符或换行符来添加空白     
要在字符串中添加制表符，可使用字符组合 \t      
要在字符串中添加换行符，可使用字符组合 \n      

- 2.3.4 　删除空白       
Python 能够找出字符串开头和末尾多余的空白。要确保字符串末尾没有空白，可使用方法 rstrip()        
实例1：        
```python
lang='   python     '
print(lang)
newlang=lang.rstrip()
print(newlang)
print(lang)
```

你还可以剔除字符串开头的空白，或同时剔除字符串两端的空白。为此，可分别使用方法 lstrip() 和 strip()      
实例2：        
```python
lang='  python  '
print(lang.rstrip())
print(lang.lstrip())
print(lang.strip())
```

### 2.4 　数字
- 2.4.1 　整数       
Python 使用两个乘号表示乘方运算：        
实例：     
```python
>>> 3 ** 2
9
>>> 3 ** 3
27
>>> 10 ** 6
1000000
```

- 2.4.3 　使用函数 str()  避免类型错误           
可调用函数 str()，它让 Python 将非字符串值表示为字符串：         
实例：     
```python
age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)
```

## <div id='class03'>第 3  章　列表简介</div>      
### 3.2 　修改、添加和删除元素         
- 3.2.2 　在列表中添加元素       
1、  在列表末尾添加元素 **append('ducati')**         
    在列表中添加新元素时，最简单的方式是将元素附加到列表末尾。给列表附加元素时，它将添加到列表末尾。继续使用前一个示例中的列表，在其末尾添加新元素 'ducati' ：
```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)
```

2、在列表中插入元素  **insert(0, 'ducati')**         
使用方法 insert() 可在列表的任何位置添加新元素。为此，你需要指定新元素的索引和值。          
```python
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)
```

- 3.2.3 　从列表中删除元素       
1、  使用 del 语句删除元素  **del motorcycles[0]**           
```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)
```

2、 使用方法 pop() 删除元素      
**方法 pop() 可删除列表末尾的元素，并让你能够接着使用它。** 术语 弹出 （ pop ）源自这样的类比：列表就像一个栈，而删除列表末尾的元素相当于弹出栈顶元素。下面从列表 motorcycles 中弹出一款摩托车：        
```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
```

3、弹出列表中任何位置处的元素         
实际上， **你可以使用 pop() 来删除列表中任何位置的元素，只需在括号中指定要删除的元素的索引即可。**         
```python
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')
```

4、根据值删除元素           
如果你只知道要删除的元素的值，可使用方法 **remove()** 。
```python
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
```

[实例](./03章、数组简介/test.py)


### 3.3 　组织列表           
- 3.3.1 　使用方法 **sort()**  对列表进行永久性排序      
```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
```

你还可以按与字母顺序相反的顺序排列列表元素，为此，只需向 sort() 方法传递参数 **reverse=True** 。           
```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)
```

- 3.3.2 　使用函数 sorted()  对列表进行临时排序(这个有点儿问题)        

- 3.3.3 　倒着打印列表 **reverse()**        
```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)
```

- 3.3.4 　确定列表的长度 **cars.__len__()** 和 **len(cars)**
```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars.__len__())
print(len(cars))
```




## <div id='class04'>第 4  章　操作列表</div> 
### 4.1 　遍历整个列表
```python
# for循环遍历
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
# for循环做更多的操作
for magician in magicians:
    print(magician.title() + ', that was a great trick!')
    print('I cannot wait wo see your next trick, ' + magician.title() + '.\n')
print('Thank you , everyone. That was a great magic show!')
```

### 4.3 　创建数值列表     
- 4.3.1 　使用函数 range()           
```python
for value in range(1, 5):
    print(value)
```
上述代码好像应该打印数字 1~5 ，但实际上它不会打印数字 5         


-  4.3.2 　使用 range()  创建数字列表            
要创建数字列表，可使用函数 list() 将 range() 的结果直接转换为列表。      
```python
numbers = list(range(1,6))
print(numbers)
```

使用函数 range() 时，还可指定步长。例如，下面的代码打印 1~10 内的偶数：     
```python
even_numbers = list(range(2,11,2))
print(even_numbers)
```

使用函数 range() 几乎能够创建任何需要的数字集.例如:         
```python
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)
```

- 4.3.3 　对数字列表执行简单的统计计算         
```python
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))
```

- 4.3.4 　列表解析           
```python
squares = [value **2 for value in range(1,11)]
print(squares)
```

[示例4.1](./04章、操作列表/示例4.1.py)


### 4.4 　使用列表的一部分       
- 4.4.1 　切片：要创建切片，可指定要使用的第一个元素和最后一个元素的索引。           
```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
```
如果你没有指定第一个索引， Python 将自动从列表开头开始：players[:4]     
要让切片终止于列表末尾，也可使用类似的语法。：players[2:]      
如果你要输出名单上的最后三名队员，可使用切片 players[-3:]     

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])
```

- 4.4.2 　遍历切片     
```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
for player in players[:3]:
    print(player)
```

- 4.4.3 复制列表 **[:]**           
```python
# 复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print(my_foods)
print(friend_foods)
print('当我们做出改变的情况的时候')
friend_foods.pop()
print(my_foods)
print(friend_foods)
```

[示例4.2](./04章、操作列表/示例4.2.py)

### 4.5 元组      
然而，有时候你需要创建一系列不可修改的元素，元组可以满足这种需求。Python 将不能修改的值称为 **不可变的** ，而不可变的列表被称为 **元组** 。         

- 4.5.1 　定义元组           
```python
dimensions = (200, 50)  # 用大括号来定义元组
print(dimensions[0])
print(dimensions[1])
dimensions[0] = 250 # 这个地方会报错，因为定义了元组，就不允许修改了
print(dimensions)
```

- 4.5.2 　遍历元组中的所有值      
```python
# 遍历元组
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)
```

- 4.5.3 　修改元组变量         
虽然不能修改元组的元素，但可以给存储元组的变量赋值。          
```python
# 修改元组变量
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
```
     

