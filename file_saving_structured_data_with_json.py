# json
import json
print(json.dumps([1, 2, 'aaa', 'bb', True, False])) # 把对象转成JSON

# 吧对象存储到文件中
with open('text.json', 'r+') as f :
    j = {'name': 'zhangpeng', 'age': 18, 'isBoy': True}
    json.dump(j, f)

# 从JSON文件中加载JSON到内存中
with open('text.json', 'r') as f :
    j = json.load(f)
    print(j)
