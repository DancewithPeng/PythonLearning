# 1.单引号字符串
str = '单引号'
print(str)

# 转义符
str2 = 'python is good, isn\'t it?'
print(str2)

# 多行字符
str3 = '''
    this is a paragraph
    
    second line
'''
print(str3)

# 字符串拼接

# + 号拼接
print(str + str2)

# 直接拼接，直接拼接不支持变量，只支持字面量
print('I am a ''Coder')

# 字符，通过索引直接访问对应的字符
print(str[0])

# [0:3] 表示一个切片
print(str[0:3])

# [:3] [0:] 可以缺省开始和结束的索引
print(str[:3], str[0:])

# 取字符串长度
print(len(str))

# python的字符串都是不可变的
