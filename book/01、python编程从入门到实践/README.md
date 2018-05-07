# 《python编程从入门到实践》 [美]Eric Matthes著       袁国忠 译

目录：     
- [第 2  章　变量和简单数据类型](#class02)
- [第 3  章　列表简介](#class03)
- [第 4  章　操作列表](#class04)
- [第 5  章　if语句](#class05)
- [第 6  章　字典](#class06)


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


## <div id='class05'>第 5  章　 if  语句</div> 

### 5.1 　一个简单示例
```python
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
```

### 5.2 　条件测试
- 5.2.5 　检查多个条件         
你可能想同时检查多个条件，例如，有时候你需要在两个条件都为 True 时才执行相应的操作。在这些情况下，关键字 **and 和 or** 可助你一臂之力。       
1、使用 and 检查多个条件 (相当于 &&)        
2、 使用 or 检查多个条件 (相当于 ||)        

- 5.2.6 　检查特定值是否包含在列表中 **使用关键字 in**         
```python
# 检查特定值是否包含在列表中
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('yanle' in requested_toppings)
```

- 5.2.7 　检查特定值是否不包含在列表中 **使用关键字 not in**        
```python
# 检查特定值是否不包含在列表中
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ', you can post a response if you wish!')
```

### 5.3 　 if 语句
- 5.3.1 　简单的 if  语句         
简单的语法结构:    
```
if conditional_test:
    do something
```

- 5.3.2 　 if-else  语句             

- 5.3.3 　 if-elif-else  结构          

- 5.3.4 　使用多个 elif  代码块         

- 5.3.5 　省略 else  代码块  Python 并不要求 if-elif 结构后面必须有 else 代码块。            

### 5.4 　使用 if 语句处理列表                
- 5.4.3 　使用多个列表     
```python
# 使用多个列表
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print('Adding ' + requested_topping + '.')
    else:
        print("Sorry, we don't have " + requested_topping + '.')
print('\nFinished making your pizza!')
```

## <div id='class06'>第 6  章　字典</div>      
在 Python 中， 字典 是一系列 键 — 值对 。每个 键 都与一个值相关联，你可以使用键来访问与之相关联的值。
  
### 6.1 　一个简单的字典            
```python
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
```

### 6.2 　使用字典       
- 6.2.1 　访问字典中的值        
```python
# 访问字典中的值
alien_0 = {'color': 'green', 'points': 5}
new_porints = alien_0['points']
print('You just earned ' + str(new_porints) + ' points!')
```

- 6.2.2 　添加键 — 值对       
```python
# 添加键值对
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
```

- 6.2.3 　先创建一个空字典       
```python
# 先创建空字典
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
```

- 6.2.4 　修改字典中的值        
```python
# 修改字典中的值
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")
```

一个简单的例子     
```python
# 一个数据字典相关的示例
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print('NEW x-position: ' + str(alien_0['x_position']))
```

- 6.2.5 　删除键 — 值对       
对于字典中不再需要的信息，可使用 **del** 语句将相应的键 — 值对彻底删除。使用 **del** 语句时，必须指定字典名和要删除的键。     
```python
# 删除键值对
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)
```

### 6.3 　遍历字典       
- 6.3.1 　遍历所有的键 — 值对        
使用的语法为： **for k, v in user_0.items()**          
```python
# 便利所有的键值对
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for key,value in user_0.items():
    print('\nkey: ' + key)
    print('value: ' + value)
```

- 6.3.2 　遍历字典中的所有键 **keys()**           
```python
# 遍历字典中的所有键
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name in favorite_languages.keys():
    print(name.title())
```

- 6.3.3 　按顺序遍历字典中的所有键       
为此，可使用函数 sorted() 来获得按特定顺序排列的键列表的副本         
```python
# 按顺序遍历字典中的所有键
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")
```

- 6.3.4 　遍历字典中的所有值 **values()**          
```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
```
为剔除重复项，可使用 **集合（ set ）**。 集合 类似于列表，但每个元素都必须是独一无二的：          
```python
# 使用set() 祛除重复项
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("The following languages have been mentioned:")
for lang in set(favorite_languages.values()):
    print(lang.title())
```      

### 6.4 　嵌套         
- 6.4.1 　字典列表       
```python
# 字典列表
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
```

代码自动生成          
```python
# 代码自动生成
aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
print(aliens.__len__())
for alien in aliens[:5]:
    print(alien)
print('......')
print('total number of aliens: ' + str(len(aliens)))
```      

- 6.4.2 　在字典中存储列表                      
示例1：        
```python
# 在字典中存列表
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
print('you order a ' + pizza['crust'] + '-crust pizza ' + 'with the flowing toppings: ' )
for topping in pizza['toppings']:
    print('\t' + topping)
```

示例2：        
```python
# 嵌套示例2
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    print('\n' + name.title() + "'s favorite languages are: ")
    for language in languages:
        print('\t' + language.title())
```

- 6.4.3 　在字典中存储字典           
```python
# 字典中存储字典
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for username,user_info in users.items():
    print('\nUsername: ' + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print('\tFull name: ' + full_name.title())
    print('\tLocation: ' + location.title())
```

## <div id='class07'>第 7 章 用户输入和while 循环</div> 
### 7.1 函数input() 的工作原理         
函数input() 让程序暂停运行，等待用户输入一些文本。获取用户输入后，Python将其存储在一个变量中，以方便你使用。           
```python
# 第一个示例
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
```

- 7.1.1 编写清晰的程序         
```python
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello, " + name + "!")
```
- 7.1.2 使用int() 来获取数值输入         
```python
# 用int() 获取用户输入的数字类型
height = input("How tall are you, in inches? ")
height = int(height)
if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
```















