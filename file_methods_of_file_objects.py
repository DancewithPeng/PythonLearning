# read函数可以自定需要读取的字节数
with open('test.json') as f :
    print(f.read(10)) # 只读取10个字节
    print(f.read())   # 继续读取完整个文件

# readline读取一行
with open('test.json') as f :
    print(f.readline())
    print(f.readline())
    print(f.readline())

# 可以用for循环读取每一行
with open('test.json') as f :
    for line in f :
        print(line, end=' ')


# 把文件的每一行读成一个list
with open('test.json') as f :
    l = list(f)
    print(l)

# 写入文件
with open('test.json', 'w') as f :
    f.write('end of writing\n')

# 其他数据类型需要转成字符串或者二进制才能写进去
with open('test.json', 'a') as f :
    value = ('the answer', 42)
    s = str(value)  # convert the tuple to string
    f.write(s)