# 生成器，用户方便创建迭代器
def reverse(data) :
    for index in range(len(data)-1, -1, -1):
        yield data[index] # 用yield返回对迭代的数据，每次调用next()会从中断处开始

for r in reverse('1234') :
    print(r)
