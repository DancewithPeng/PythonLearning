# 读取文件，为了安全，推荐用with关键字打开文件
with open('test.json') as f :
    file_data = f.read()
    print(file_data)

print(f.closed)