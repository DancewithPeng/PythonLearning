# 数组
arr = [1, 2, 3, 4, 5, 6]
print(arr)

# 除数组元素，通过索引
print(arr[0])

# 数组也支持切片
print(arr[0:2], arr[2:])

# 数组拼接，数组也支持*运算符
arr2 = arr[0:2] * 2 + arr[2:]
print(arr2)

# 不支持-符号
# print(arr2 - arr[2:])

# 元素个数
print(len(arr))