# 集合，用{}表示，集合是无序的
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

# 判断对象是否是集合中的元素
print('apple' in basket)
print('orange' in basket)
print('abc' in basket)

# 通过字面量来初始化一个集合
a = set('abcdefgh')
b = set('efgh')
print(a, b)

# 可以进行排除操作
print(a-b)

# 可以进行合并操作
print(a | b)

# 可以进行取交集操作
print(a & b)

# 可以进行排除操作
print(a ^ b)

# 集合也支持集合推导
s = { x for x in range(10) }
print(s)