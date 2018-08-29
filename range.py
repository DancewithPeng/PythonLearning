# 范围函数range()

# 表示0到5
for i in range(5) :
    print(i)

# 表示5-10，不包含10
for i in range(5, 10) :
    print(i)

# 表示0，10，中间隔3
for i in range(0, 10, 3) :
    print(i)

# 表示-10 到 -100，中间隔-30
for i in range(-10, -100, -30):
    print(i)

# 根据range来创建list
print(list(range(5)))