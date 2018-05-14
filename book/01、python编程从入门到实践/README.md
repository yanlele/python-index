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

-  7.1.3 求模运算符 **求模运算符 (%)**            


### 7.2 while 循环简介              
在用户选择的时候退出          
```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
```

- 7.2.4 使用break 退出循环            
要立即退出while 循环，不再运行循环中余下的代码，也不管条件测试的结果如何，可使用break 语句。            
```python
# break的使用
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")
```

- 7.2.5 在循环中使用continue         
要返回到循环开头，并根据条件测试结果决定是否继续执行循环，可使用continue 语句，它不像break 语句那样不再执行余下的代码并退出整个循环。例如，来看一个从1数 到10，但只打印其中偶数的循环:           
```python
# continue
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
``` 

### 7.3 使用while 循环来处理列表和字典          
- 7.3.1 在列表之间移动元素           
```python
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# 验证每个用户，直到没有未验证用户为止
# 将每个经过验证的列表都移到已验证用户列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
# 显示所有已验证的用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
```

- 7.3.2 删除包含特定值的所有列表元素      
```python
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)
```

- 7.3.3 使用用户输入来填充字典         
```python
responses = {}
flag = True
while flag:
    name = input('请输入你的名字')
    response = input('请输入你的答案')
    responses[name] = response
    repeat = input('是否继续下一个人问答？yes/no')
    if (repeat != 'yes'):
        flag = False
for name, response in responses.items():
    print(name, response)
```


## <div id='class08'>第 8 章 函数</div>
### 8.1 定义函数            
```python
def get_user(name):
    print(name)


get_user('yanle')
```

### 8.2 传递实参
- 8.2.2 　关键字实参          
```python
# 关键字实参
def describe_pet(animal_type, pet_name):
    """ 显示宠物的信息 """
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet(animal_type='hamster', pet_name='harry')
```
关键字实参的顺序无关紧要，因为 Python 知道各个值该存储到哪个形参中。下面两个函数调用是等效的：         
```python
def describe_pet(animal_type, pet_name):
    """ 显示宠物的信息 """
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
    
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')
```

- 8.2.3 　默认值            
```python
# 默认值
def describe_pet(pet_name, animal_type='dog'):
    """ 显示宠物的信息 """
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    

describe_pet(pet_name='willie')
```
如果要描述的动物不是小狗，可使用类似于下面的函数调用：         
```
describe_pet(pet_name='harry', animal_type='hamster')
```

- 8.2.4 　等效的函数调用            
```
#  一条名为 Willie 的小狗
describe_pet('willie')
describe_pet(pet_name='willie')

#  一只名为 Harry 的仓鼠
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')
```

### 8.3 　返回值            
- 8.3.1 　返回简单值          
```python
# 简单的返回值示例
def get_name(first_name, last_name):
    full_name = first_name + last_name
    return full_name


musican = get_name('yan', 'le')
print(musican)
```

- 8.3.2 　让实参变成可选的           
```python
def get_name (first_name, last_name, middle_name):
    if middle_name:
        full_name = first_name + middle_name +last_name
    else:
        full_name = first_name + middle_name
    return full_name


my_name = get_name('yan ', 'le', 'le')
print(my_name)
```

- 8.3.3 　返回字典           
```python
def build_person(first_name, last_name):
    person = {'first_name': first_name, 'last_name': last_name}
    return person


get_person = build_person('yanle', 'le')
print(get_person)
```

- 8.3.4 　结合使用函数和 while  循环              
```python
def get_name(first_name, last_name):
    return first_name + last_name


while True:
    print('输入你的名字')
    print('输入q退出程序')
    first_name = input('First name: ')
    if first_name == 'q':
        break
    last_name = input('Last name: ')
    if last_name == 'q':
        break
    full_name = get_name(first_name, last_name)
    print(full_name)
```

### 8.4 　传递列表         
- 8.4.1 　在函数中修改列表         
```python
# 在函数中修改列表
def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表 completed_models 中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        #  模拟根据设计制作 3D 打印模型的过程
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """ 显示打印好的所有模型 """
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
```

## 8.5 　传递任意数量的实参            
函数只有一个形参 *toppings ，但不管调用语句提供了多少实参，这个形参都将它们统统收入囊中：          
```python
# 传递任意数量的实参
def make_pizza(*toppings):
    """ 概述要制作的比萨 """
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
```           

- 8.5.1 　结合使用位置实参和任意数量实参            
如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后。           
```python
def make(size, *toppings):
    print('\nsize ' + str(size) + '-inch pizza with the following toppings')
    for topping in toppings:
        print('-' + topping)


make(16, 'yan')
make(12, 'yanle', 'lele', 'bilibli')
```

- 8.5.2 　使用任意数量的关键字实参           
有时候，需要接受任意数量的实参，但预先不知道传递给函数的会是什么样的信息。在这种情况下，可将函数编写成能够接受任意数量的键 — 值对 —— 调用语句提供了多少就接受多少。           
```python
# 使用任意数量的关键字实参
def build_profile(first, last, **user_info):
    """ 创建一个字典，其中包含我们知道的有关用户的一切 """
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)
```

### 8.6 　将函数存储在模块中      
- 8.6.1、导入整个模块            
要让函数是可导入的，得先创建模块。 模块 是扩展名为 .py 的文件，包含要导入到程序中的代码。            
例如我们建立一个test.py的模块文件：           
```python
a = 7


def make_pizza(size, *toppings):
    print('\n披萨的大小为： ' + str(size))
    for topping in toppings:
        print('- ' + topping)
```

接下来，我们在 test.py 所在的目录中创建另一个名为 making_pizzas.py 的文件，这个文件导入刚创建的模块，再调用 make_pizza() 两次：
```python
import test


test.make_pizza(16, 'pepperoni')
test.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
print(test.a)
```
通过这个语法来实现的调用： **module_name.function_name()**               

- 8.6.2、导入特定的函数           
你还可以导入模块中的特定函数，这种导入方法的语法如下：**from module_name import function_name**                
通过用逗号分隔函数名，可根据需要从模块中导入任意数量的函数：**from module_name import function_0, function_1, function_2**            

- 8.6.3、使用 as  给函数指定别名            
通用语法如下：**from module_name import function_name as fn**          
```python
from pizza import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
```

- 8.6.4 　使用 as  给模块指定别名         
你还可以给模块指定别名。通过给模块指定简短的别名（如给模块 pizza 指定别名 p ），让你能够更轻松地调用模块中的函数。          
```python
import pizza as p
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

- 8.6.5 　导入模块中的所有函数         
使用星号（ * ）运算符可让 Python 导入模块中的所有函数：               
```python
from pizza import *
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

## <div id='class089>第 9 章 类</div>

### 9.1 　创建和使用类         
- 9.1.1 　创建 Dog  类          
根据 Dog 类创建的每个实例都将存储名字和年龄。我们赋予了每条小狗蹲下（ sit() ）和打滚（ roll_over() ）的能力              
```python
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + ' is now sitting.')

    def roll_over(self):
        print(self.name.title() + ' rolled over!')
```

9.1.1.1、方法 __init__()           
类中的函数称为 方法 ；        
方法 __init__() 是一个特殊的方法，每当你根据 Dog 类创建新实例时， Python 都会自动运行它。           
**我们将方法 __init__() 定义成了包含三个形参： self 、 name 和 age 。在这个方法的定义中，形参 self 必不可少，还必须位于其他形参的前面。**        
因为 Python 调用这个 __init__() 方法来创建 Dog 实例时，将自动传入实参 self 。每个与类相关联的方法调用都自动传递实参 self ，它是一个指向实例本身的引用，让实例能够访问类中的属性和方法。          
self.name = name 获取存储在形参 name 中的值，并将其存储到变量 name 中，然后该变量被关联到当前创建的实例。 self.age = age 的作用与此类似。像这样可通过实例访问的变量称为 **属性**               

- 9.1.2 　根据类创建实例            
```python
class Dog():
    # 省略

my_dog = Dog('hillie', 6)
print('my dog name is ' + my_dog.name.title() + ' .')
print('my dog age is ' + str(my_dog.age)+ 'yours lod')
```

调用方法            
根据 Dog 类创建实例后，就可以使用句点表示法来调用 Dog 类中定义的任何方法。          
```python
class Dog():
    # 省略

my_dog = Dog('hillie', 6)
print('my dog name is ' + my_dog.name.title() + ' .')
print('my dog age is ' + str(my_dog.age)+ 'yours lod')
my_dog.sit()
my_dog.roll_over()
```

创建多个实例            
```python
class Dog():
    --snip--
    
my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()
```


### 9.2 　使用类和实例         
- 9.2.1 　 Car  类          
下面来编写一个表示汽车的类，它存储了有关汽车的信息，还有一个汇总这些信息的方法：            
```python
class Car():
    """ 一次模拟汽车的简单尝试 """
    def __init__(self, make, model, year):
        """ 初始化描述汽车的属性 """
        self.make = make
        self.model = model
        self.year = year
    def get_descriptive_name(self):
        """ 返回整洁的描述性信息 """
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
```

- 9.2.2 　给属性指定默认值               
**self.odometer_reading = 0**就是默认值                     
```python
class Car():
    def __init__(self, make, model, year):
        """ 初始化描述汽车的属性 """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        print('这里是其他代码块')

    def read_odometer(self):
        """ 打印一条指出汽车里程的消息 """
        print("This car has " + str(self.odometer_reading) + " miles on it.")


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
```            


### 9.3 　继承               
一个典型的继承案例：          
```python
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print('this car his ' + str(self.odometer_reading) + ' miles on it')

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('you cannot roll back an odometer! ')

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print('我要给车加油！')


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super(ElectricCar, self).__init__(make, model, year)
        self.battery_size = 80

    def describe_battery(self):
        print('这辆车现在还有的电量为： ' + str(self.battery_size))

    def fill_gas_tank(self):
        print('电瓶车根本就不需要汽油')


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()
```
这个例子实现了继承父类，同事给子类定义属于自己的属性和方法，还展示了如何重新父类的方法：                
          
- 9.3.5 　将实例用作属性                
非常经典一个实例！！！！                        
```python
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print('this car his ' + str(self.odometer_reading) + ' miles on it')

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('you cannot roll back an odometer! ')

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print('我要给车加油！')


class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print('这辆车现在还有的电量为： ' + str(self.battery_size))


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super(ElectricCar, self).__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print('电瓶车根本就不需要汽油')


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.fill_gas_tank()
my_tesla.battery.describe_battery()
```

下面是一个类的扩展，如果子类继承了父类的属性和方法，而且有太多自己独有的东西，我们就可以把子类独有的东西，抽象出来，这个抽象出来的对象，可以单独作为一个类，然后可以将这个实例对象作为一个属性，传给子类：               
```python
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print('this car his ' + str(self.odometer_reading) + ' miles on it')

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('you cannot roll back an odometer! ')

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print('我要给车加油！')


class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print('这辆车现在还有的电量为： ' + str(self.battery_size))

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = '这辆车最大的城市里程为： ' + str(range) + ' ,这个里程是在充满电的前提条件下的'
        print(message)


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super(ElectricCar, self).__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print('电瓶车根本就不需要汽油')


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.fill_gas_tank()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
```

**9.4 　导入类**