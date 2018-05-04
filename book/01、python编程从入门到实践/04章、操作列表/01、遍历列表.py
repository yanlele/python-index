# for循环遍历
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# for循环做更多的操作
for magician in magicians:
    print(magician.title() + ', that was a great trick!')
    print('I cannot wait wo see your next trick, ' + magician.title() + '.\n')
print('Thank you , everyone. That was a great magic show!')