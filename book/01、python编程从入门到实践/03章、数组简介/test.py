person = ['杜鹏', '许海峰', '郭涛']
print(person)
print(person[person.__len__() - 1] + ' 不能来了')
removeName = person[person.__len__() - 1]
person.remove(removeName)
print('我需要重新邀请小伙伴儿')
person.append('王大叔')
print(person)
print('-------------------')
print('我需要邀请更加多的小伙伴儿来参加')
person.insert(0, '嗷大喵')
person.insert(int(person.__len__() / 2), '王老吉')
person.append('胡大胖')
print('现在我的小伙伴儿们有：', person)
print('-------------------')
print('刚刚接到消息，我只能邀请两位小伙伴儿来参加会议了')
while person.__len__() != 2:
    popName = person.pop()
    print('不能邀请的小伙伴儿是： ', popName)

for friend in person:
    print(friend, ' 依然在参加会议队列中')

print('会议要结束了，我的小伙伴们都要回去了')

del person[1]
del person[0]

print('现在我的会议场中的小伙伴儿为：', person)