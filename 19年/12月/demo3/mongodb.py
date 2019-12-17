

client=MongoClient(host='10.90.9.101',port=27017)
client=MongoClient(host='10.90.9.102',port=27018)
client=MongoClient(host='10.90.9.101:27018,10.90.9.102:27018,10.90.9.103:27018')
db.client.myDB
db.conn.get_datebase("myDB")
db=client.test
coll=db.get_collection("mycollection")
post_date={
   '_id':'10',
   'item':'book1',
   'qty':18
}
result=coll.insert_one(post_date)
print(result)
post_1={'_id:'11','item':'book1','qty':18}
post_2={'_id:'12','item':'book1','qty':18}
post_3={'_id:'13','item':'book1','qty':18}

new_result=coll.insert_many({post_1,post_2,post_3})

find_post=coll.find_one({'item':'book'})
find_post=coll.find({'item':'book1'})

condition=('item':'book')
pty{'$set':{'pty':22}}
result=col.update(condition,pty)



