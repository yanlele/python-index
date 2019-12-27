def hub(ss, x=2.0, y=4.0):
    # ss = 10, x = 3, y = 4
    # ss = ss + x * y
    ss += x * y
    return ss

ss = 10

print(ss, hub(ss, 3))
