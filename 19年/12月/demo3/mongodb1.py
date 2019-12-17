import pymongo

client = pymongo.MongoClient("mongodb://192.168.205.10:27017/")
db = client["my_db"]

my_col = db["sites"]

# 插入一条数据
my_dict = {
    'name': 'hudie',
    'alexa': 10000,
}

x = my_col.insert_one(my_dict)
print(x.inserted_id)
