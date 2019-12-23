from pymongo import MongoClient

# 建立MongoDB数据库连接
client = MongoClient('localhost', 27017)
db = client.mydb
coll = db.get_collection("myCollection")
# post_data = {  '_id': '222',  'item' : 'book',   'qty': 20
# }
# result = coll.insert_one(post_data)
# print(result)


# '''插入多条'''
# post_1 = {     '_id': '11',     'item' : 'book1',     'qty': 18 }
# post_2 = {     '_id': '12',     'item' : 'book1',     'qty': 18 }
# post_3 = {     '_id': '13',     'item' : 'book1',     'qty': 18 }
# new_result = coll.insert_many([post_1,post_2,post_3])
#
# '''查询'''
find_post = coll.find_one({'item': 'book'})
find_posts = coll.find({'item': 'book1'})
print("find_post", find_post)
for i in find_posts:
    print("find_posts", i)
#
# '''修改'''
condition = {'item': 'book'}
qty = {'$set': {'qty': 22}}
result = coll.update(condition, qty)
#
# '''删除'''
result = coll.remove({'item': 'book1'})
result = coll.delete_one({'item': 'book'})
result = coll.delete_many({'_id': '14'})
# print(result)
# '''
