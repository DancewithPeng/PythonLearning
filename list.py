# 列表
L = []

# 追加元素
L.append(100)
print(L)

# 扩展元素，相当于追加一个数组
e = [1, 2, 3]
L.extend(e)
print(L)

# 插入一个元素
L.insert(0, 10086)
print(L)

# 移除一个元素
L.remove(1)
print(L)

# list支持栈的pop操作
last = L.pop()
print(last, L)

# 清空列表
L.clear()
print(L)

# 返回元素的位置
L.extend([1, 2, 88, 100, 99, 88])
i = L.index(88) # 如果有多个一样的元素，会先找到第一个元素
print(i, L[i], L)

# index()函数可以指定查找的起始和结束位置
i2 = L.index(88, 3, 6)
print(i2, L[i2], L)

# 统计列表中相同元素的个数
c = L.count(88)
print(c, L)

# 排序
print('排序前：', L)
L.sort()
print('排序后', L)

# 反转列表
print('反转前：', L)
L.reverse()
print('反转后：', L)

# 拷贝
L2 = L.copy()
L[0] = 10010
print(L, L2)