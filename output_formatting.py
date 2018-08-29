# 插值输出
year = 2018
event = 'Referendum'

# 在字符串前加f或F，可以使用插值形式的拼接字符串
print(f'Results of the {year} {event}')

# 另外一种使用占位符的方式是string.format()
yes_votes = 42_572_654 ; no_votes = 43_132_495
percentage = yes_votes/(yes_votes+no_votes)
print('{:-9} Yes votes {:2.2%}'.format(yes_votes, percentage))

# str()方法，把对象转成人类可读的形式展现出来，返回值一定是字符串
# 而repr()方法则是表示解释器可读的代码，做类型判断，返回值不一是字符串
s = 'hello world\n'
print(str(s))
print(repr(s))

i = 100
print(str(i))
print(repr(i))

f = 0.001
print(str(f))
print(repr(f))

x = 10 * 3.25
y = 200 * 200
print(repr((x, y, 'errg', 'demo')))

