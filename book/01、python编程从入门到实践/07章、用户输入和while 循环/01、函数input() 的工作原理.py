# 第一个示例
# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)

# 编写清晰的程序
# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "
# name = input(prompt)
# print("\nHello, " + name + "!")

# 用int() 获取用户输入的数字类型
height = input("How tall are you, in inches? ")
height = int(height)
if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
