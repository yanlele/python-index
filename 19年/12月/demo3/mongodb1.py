import pymongo

# 建立 mongodb 的链接
client = pymongo.MongoClient("mongodb://192.168.205.10:27017/")
db = client["my_db"]

my_col = db["sites"]

# 插入一条数据
# my_dict = {
#     '_id': '1231231231',
#     'name': 'hudie',
#     'item': 'book',
#     'qty': 20
# }
# insert_one_result = my_col.insert_one(my_dict)
# print(insert_one_result)

# 一次性插入多条数据
# post_1 = {'_id': '11', 'name': 'hudie', 'item': 'book1', 'qty': 18}
# post_2 = {'_id': '12', 'name': 'hudie', 'item': 'book1', 'qty': 18}
# post_3 = {'_id': '13', 'name': 'hudie', 'item': 'book1', 'qty': 18}
# new_result = my_col.insert_many([post_1, post_2, post_3])

# 查询
# find_post = my_col.find_one({'_id': '13'})
# find_posts = my_col.find({'name': 'hudie'})
# print("find_post", find_post)
# print('---------')
# for i in find_posts:
#     print("find_posts", i)

# 修改数据
# condition = {'item': 'book1'}
# qty = {'$set': {'item': 'book123'}}
# result = my_col.update(condition, qty)

# 删除数据
my_col.remove({'item': 'book123'})
my_col.delete_one({'_id': '1231231231'})
my_col.delete_many({'item': 'book'})
