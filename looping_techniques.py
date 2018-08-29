# 字典可以通过items函数同时返回key和value
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items() :
    print(k, v)

# 数组可以通过enumerate函数，同时返回index和value
arr = ['I', 'am', 'a', 'coder']
for i, v in enumerate(arr) :
    print(i, v)

# 同时遍历两个序列时，可以用zip函数，这个函数会自动取最小集合的
questions = ['name', 'quest', 'favorite color', 'love', '1234']
answers = ['lancelot', 'the holy grail', 'blue', 'abc']
for q, a in zip(questions, answers) :
    print(q, a)

# 反向遍历
s = [x for x in range(1, 10, 2)]
print(s)
for e in reversed(s) :
    print(e)

# 排序遍历，这里set是为了过滤重复项
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)) :
    print(f)

# 创建新的序列是更安全的做法
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data : 
    if not math.isnan(value) :
        filtered_data.append(value)

print(filtered_data)